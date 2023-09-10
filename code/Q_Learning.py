import numpy as np

def move(loc, dir):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]

def is_valid_move(loc, my_map):
    return 0 <= loc[0] < len(my_map) and 0 <= loc[1] < len(my_map[0]) and not my_map[loc[0]][loc[1]]

def build_constraint_table(constraints, agent):
    constraint_table = []

    # task 4
    for constraint in constraints:
        if 'positive' not in constraint:
            constraint['positive'] = False
        if constraint['agent'] == agent:
            constraint_table.append(constraint)
        if constraint['agent'] != agent and constraint['positive'] == True:
            if len(constraint['loc']) == 2:
                con = {'agent': agent, 'loc': [constraint['loc'][1], constraint['loc'][0]],
                       'timestep': constraint['timestep'], 'positive': False}
                constraint_table.append(con)
            else:
                con = {'agent': agent, 'loc': [constraint['loc'][0]],
                       'timestep': constraint['timestep'], 'positive': False}
                constraint_table.append(con)

    return constraint_table
    pass


def is_constrained(curr_loc, next_loc, next_time, constraint_table):

    # task 4
    for constraint in constraint_table:
        if constraint['positive']:
            if len(constraint['loc']) == 1:
                if next_time == constraint['timestep'] and next_loc == constraint['loc'][0]:
                    return 1
            else:
                if next_time == constraint['timestep'] and next_loc == constraint['loc'][1] and curr_loc == \
                        constraint['loc'][0]:
                    return 1
        else:
            if len(constraint['loc']) == 1:
                if next_time == constraint['timestep'] and next_loc == constraint['loc'][0]:
                    return 2
            else:
                if next_time == constraint['timestep'] and next_loc == constraint['loc'][1] and curr_loc == \
                        constraint['loc'][0]:
                    return 2
    return 0

    pass

def Q_learning(my_map, start_loc, goal_loc, h_values, agent, constraints):
    alpha = 0.9
    gamma = 0.9
    epsilon = 0.2
    num_actions = 5

    constraint_table = build_constraint_table(constraints, agent)
    Q_table = np.zeros((len(my_map), len(my_map[0]), num_actions))

    for episode in range(1000):
        curr_loc = start_loc
        time_step = 0  # Reset time_step for each episode
        total_reward = 0  # Track total reward for debugging

        while curr_loc != goal_loc:
            if not is_valid_move(curr_loc, my_map):
                break

            if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice(num_actions)
            else:
                action = np.argmax(Q_table[curr_loc[0], curr_loc[1], :])

            next_loc = move(curr_loc, action)
            constraint_type = is_constrained(curr_loc, next_loc, time_step, constraint_table)  # Use time_step

            if constraint_type == 2 or not is_valid_move(next_loc, my_map):
                reward = -100  # penalty for invalid move
                next_max = 0
            elif constraint_type == 1:
                reward = 100  # reward for following positive constraint
                next_max = np.max(Q_table[next_loc[0], next_loc[1], :])
            elif next_loc == goal_loc:
                reward = 100  # reward for reaching the goal
                next_max = 0
            else:
                reward = -1  # small penalty for each step
                next_max = np.max(Q_table[next_loc[0], next_loc[1], :])

            # Q-learning update rule
            Q_table[curr_loc[0], curr_loc[1], action] += alpha * (reward + gamma * next_max - Q_table[curr_loc[0], curr_loc[1], action])

            curr_loc = next_loc
            time_step += 1  # Increment time_step
            total_reward += reward  # Update total reward

        # print(f"Episode {episode}: Total reward = {total_reward}")  # Print total reward for debugging

    # Extract the optimal path using the learned Q-values
    curr_loc = start_loc
    path = [curr_loc]
    max_attempts = len(my_map) * len(my_map[0])  # Set a maximum number of attempts to extract the path
    attempts = 0

    while curr_loc != goal_loc and attempts < max_attempts:
        action = np.argmax(Q_table[curr_loc[0], curr_loc[1], :])
        curr_loc = move(curr_loc, action)
        path.append(curr_loc)
        attempts += 1

    return path


# def Q_learning(my_map, start_loc, goal_loc, h_values, agent, constraints):
#     alpha = 0.9
#     gamma = 0.9
#     epsilon = 0.2  # for epsilon-greedy exploration
#     num_actions = 5  # 4 directions + stay in place
#
#     constraint_table = build_constraint_table(constraints, agent)
#     Q_table = np.zeros((len(my_map), len(my_map[0]), num_actions))
#
#     for episode in range(1000):  # number of training episodes
#         curr_loc = start_loc
#         while curr_loc != goal_loc:
#             # Ensure that the current location is within the bounds of the map
#             if not is_valid_move(curr_loc, my_map):
#                 break
#
#             if np.random.uniform(0, 1) < epsilon:
#                 # epsilon-greedy exploration
#                 action = np.random.choice(num_actions)
#             else:
#                 action = np.argmax(Q_table[curr_loc[0], curr_loc[1], :])
#
#             next_loc = move(curr_loc, action)
#
#             # Check constraints
#             constraint_type = is_constrained(curr_loc, next_loc, episode, constraint_table)
#             if constraint_type == 2 or not is_valid_move(next_loc, my_map):
#                 reward = -100  # penalty for invalid move
#                 next_max = 0
#             elif constraint_type == 1:
#                 reward = 100  # reward for following positive constraint
#                 next_max = np.max(Q_table[next_loc[0], next_loc[1], :])
#             elif next_loc == goal_loc:
#                 reward = 100  # reward for reaching the goal
#                 next_max = 0
#             else:
#                 reward = -1  # small penalty for each step
#                 next_max = np.max(Q_table[next_loc[0], next_loc[1], :])
#
#             # Q-learning update rule
#             Q_table[curr_loc[0], curr_loc[1], action] += alpha * (reward + gamma * next_max - Q_table[curr_loc[0], curr_loc[1], action])
#
#             curr_loc = next_loc
#
#     # Extract the optimal path using the learned Q-values
#     curr_loc = start_loc
#     path = [curr_loc]
#     while curr_loc != goal_loc:
#         action = np.argmax(Q_table[curr_loc[0], curr_loc[1], :])
#         curr_loc = move(curr_loc, action)
#         path.append(curr_loc)
#
#     return path
