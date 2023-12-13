import heapq


def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]


def compare_nodes(n1, n2):
    """Return true is n1 is better than n2."""
    return n1['g_val'] + n1['h_val'] < n2['g_val'] + n2['h_val']


def sort_sets(set_list):
    for i in range(len(set_list) - 1):
        for j in range(len(set_list) - i - 1):
            if set_list[j]['bound'] < set_list[j + 1]['bound']:
                temp = set_list[j]
                set_list[j] = set_list[j + 1]
                set_list[j + 1] = temp
    return set_list


def LRTA_star(my_map, start_loc, goal_loc, h_values, agent, constraints):
    while True:
        path, changed = LRAT_trial(my_map, start_loc, goal_loc, h_values)
        if not changed:
            return path


def LRAT_trial(my_map, start_loc, goal_loc, h_values):
    path = []
    x = start_loc
    path.append(x)
    flag = False
    while x != goal_loc:
        y, dummy = look_ahead_update(x, h_values, my_map)
        flag = flag or dummy
        path.append(y)
        x = y

    return path, flag


def look_ahead_update(x, h_values, my_map):
    temp = float('inf')
    y = x
    for dir in range(4):
        child_loc = move(x, dir)
        if child_loc[0] <= -1 or child_loc[1] <= -1:
            continue
        if child_loc[0] >= len(my_map) or child_loc[1] >= len(my_map[0]):
            continue
        if my_map[child_loc[0]][child_loc[1]]:
            continue
        if 1 + h_values[child_loc] < temp:
            y = child_loc
            temp = 1 + h_values[child_loc]
    if h_values[x] < 1 + h_values[y]:
        h_values[x] = 1 + h_values[y]
        return y, True
    else:
        return y, False
