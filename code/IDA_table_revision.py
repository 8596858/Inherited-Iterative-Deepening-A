def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]


def tt_IDA(my_map, start_loc, goal_loc, h_values, agent, constraints):
    transposition_table = dict()
    earliest_goal_timestep = 0
    # traversed_nodes = [0]
    path_list = []

    # make sure h_values has start_loc
    flag = False
    for h in h_values:
        if h == start_loc:
            flag = True
            break
    if not flag:
        return None, 0  # Failed to find solutions

    h_value = h_values[start_loc]
    # constraint_table = build_constraint_table(constraints, agent)
    constraint_table = []
    path_list.append(start_loc)
    bound = h_value
    while True:
        bound, flag = DeepSearch(my_map, bound, path_list, h_values, constraint_table, earliest_goal_timestep, transposition_table)
        if flag:
            return path_list
        if bound == float("inf"):
            return None, 0


def DeepSearch(my_map, bound, path_list, h_values, constraints, earliest_goal_timestep, transposition_table):
    succ = []
    b = []
    curr = path_list[len(path_list) - 1]
    if h_values[curr] == 0:
        return bound, True
    new_bound = float("inf")
    for dir in range(4):
        if dir < 4:
            child_loc = move(path_list[len(path_list) - 1], dir)
        else:
            child_loc = path_list[len(path_list) - 1]
        if child_loc[0] <= -1 or child_loc[1] <= -1:
            continue
        if child_loc[0] >= len(my_map) or child_loc[1] >= len(my_map[0]):
            continue
        if my_map[child_loc[0]][child_loc[1]]:
            continue
        succ.append(child_loc)
        if child_loc in transposition_table:
            b.append(1 + transposition_table[child_loc])
        else:
            b.append(1 + h_values[child_loc])
    for i in range(len(succ)):
        for j in range(len(succ)):
            if b[i] > b[j]:
                temp1 = succ[i]
                temp2 = b[i]
                succ[i] = succ[j]
                b[i] = b[j]
                succ[j] = temp1
                b[j] = temp2

    for i in range(len(succ)):
        path_list.append(succ[i])
        flag = False
        if b[i] <= bound:
            temp, flag = DeepSearch(my_map, bound-1, path_list, h_values, constraints, earliest_goal_timestep, transposition_table)
            temp = temp + 1
        else:
            temp = b[i]
        if flag:
            return temp, flag
        new_bound = min(new_bound, temp)
        path_list.pop()
    transposition_table[curr] = new_bound
    return new_bound, False