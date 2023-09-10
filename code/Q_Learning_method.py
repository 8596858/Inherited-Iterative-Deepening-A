import heapq
import numpy as np


def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]


def get_sum_of_cost(paths):
    rst = 0
    for path in paths:
        rst += len(path) - 1
    return rst


def compute_heuristics(my_map, goal):
    # Use Dijkstra to build a shortest-path tree rooted at the goal location
    open_list = []
    closed_list = dict()
    root = {'loc': goal, 'cost': 0}
    heapq.heappush(open_list, (root['cost'], goal, root))
    closed_list[goal] = root
    while len(open_list) > 0:
        (cost, loc, curr) = heapq.heappop(open_list)
        for dir in range(4):
            child_loc = move(loc, dir)
            child_cost = cost + 1
            if child_loc[0] < 0 or child_loc[0] >= len(my_map) \
                    or child_loc[1] < 0 or child_loc[1] >= len(my_map[0]):
                continue
            if my_map[child_loc[0]][child_loc[1]]:
                continue
            child = {'loc': child_loc, 'cost': child_cost}
            if child_loc in closed_list:
                existing_node = closed_list[child_loc]
                if existing_node['cost'] > child_cost:
                    closed_list[child_loc] = child
                    # open_list.delete((existing_node['cost'], existing_node['loc'], existing_node))
                    heapq.heappush(open_list, (child_cost, child_loc, child))
            else:
                closed_list[child_loc] = child
                heapq.heappush(open_list, (child_cost, child_loc, child))

    # build the heuristics table
    h_values = dict()
    for loc, node in closed_list.items():
        h_values[loc] = node['cost']
    return h_values


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


def get_location(path, time):
    if time < 0:
        return path[0]
    elif time < len(path):
        return path[time]
    else:
        return path[-1]  # wait at the goal location


def get_path(goal_node):
    path = []
    curr = goal_node
    while curr is not None:
        path.append(curr['loc'])
        curr = curr['parent']
    path.reverse()
    return path


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


def push_node(open_list, node):
    heapq.heappush(open_list, (node['g_val'] + node['h_val'], node['h_val'], node['loc'], node))


def pop_node(open_list):
    _, _, _, curr = heapq.heappop(open_list)
    return curr


def compare_nodes(n1, n2):
    """Return true is n1 is better than n2."""
    return n1['g_val'] + n1['h_val'] < n2['g_val'] + n2['h_val']


def Q_learning(my_map, start_loc, goal_loc, h_values, agent, constraints):
    constraint_table = build_constraint_table(constraints, agent)
    Q_table = np.ones([len(my_map) + 2, len(my_map[0]) + 2, 5], dtype=float)
    for i in range(len(my_map) * len(my_map[0])):
        curr = {'loc': start_loc, 'g_val': 0, 'parent': None, 'timestep': 0}
        while curr['loc'] != goal_loc and \
                curr['loc'] != -1 and \
                curr['loc'] != -1 and \
                curr['loc'] != len(my_map) and \
                curr['loc'] != len(my_map[0]) and \
                (not my_map[curr['loc'][0]][curr['loc'][1]]):
            flag = float('-inf')
            next_dir = 0
            for dir in range(5):
                # print("!!!!!!!!!!")
                # print(Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir])
                child_loc = move(curr['loc'], dir)
                Qmax = max(Q_table[child_loc[0] + 1, child_loc[1] + 1, 0:4])
                if child_loc != goal_loc and \
                        is_constrained(curr['loc'], child_loc, curr['timestep'] + 1, constraint_table) == 0 and \
                        child_loc[0] != -1 and \
                        child_loc[1] != -1 and \
                        child_loc[0] != len(my_map) and \
                        child_loc[1] != len(my_map[0]) and \
                        (not my_map[child_loc[0]][child_loc[1]]):
                    Q_table[curr['loc'][0] + 1, curr['loc'][1], dir] = round(Q_table[curr['loc'][0] + 1, curr['loc'][1], dir] + float(0.9) * (float(0.9 * Qmax) - Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir]), 4)
                elif is_constrained(curr['loc'], child_loc, curr['timestep'] + 1, constraint_table) == 0 or \
                        child_loc[0] == -1 or \
                        child_loc[1] == -1 or \
                        child_loc[0] == len(my_map) or \
                        child_loc[1] == len(my_map[0]) or \
                        my_map[child_loc[0]][child_loc[1]]:
                    Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir] = round(Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir] + float(0.9) * (float(-1 + 0.9 * Qmax) - Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir]), 4)
                else:
                    Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir] = round(Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir] + float(0.9) * (float(1 + 0.9 * Qmax) - Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir]), 4)
                if Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir] > flag:
                    next_dir = dir
                    flag = Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir]
            temp = {'loc': move(curr['loc'], next_dir),
                    'g_val': curr['g_val'] + 1,
                    'parent': curr,
                    'timestep': curr['timestep'] + 1}
            curr = temp
    print(Q_table)
    path = [start_loc]
    next_loc = start_loc
    while next_loc != goal_loc and \
            next_loc[0] != -1 and \
            next_loc[1] != -1 and \
            next_loc[0] != len(my_map) and \
            next_loc[1] != len(my_map[0]) and \
            not my_map[next_loc[0]][next_loc[1]]:
        flag = move(next_loc, 0)
        child_loc = next_loc
        for dir in range(5):
            child_loc = move(next_loc, dir)
            if flag < Q_table[child_loc[0] + 1, child_loc[1] + 1, dir]:
                next_loc = child_loc
        path.append(child_loc)
    if path[len(path) - 1] == goal_loc:
        return path
    else:
        return None