import heapq


def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]


def get_sum_of_cost(paths):
    rst = 0
    for path in paths:
        rst += len(path) - 1
    return rst


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
        if len(constraint['loc']) == 1:
            if next_time == constraint['timestep'] and next_loc == constraint['loc'][0]:
                return 1
        else:
            if next_time == constraint['timestep'] and next_loc == constraint['loc'][1] and curr_loc == \
                    constraint['loc'][0]:
                return 1
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


def sort_sets(set_list):
    for i in range(len(set_list) - 1):
        for j in range(len(set_list) - i - 1):
            if set_list[j]['bound'] < set_list[j + 1]['bound']:
                temp = set_list[j]
                set_list[j] = set_list[j + 1]
                set_list[j + 1] = temp
    return set_list


def LRTA_star(my_map, start_loc, goal_loc, h_values, agent, constraints):
    traversed_nodes = [0]
    while True:
        path, changed = LRAT_trial(my_map, start_loc, goal_loc, h_values, traversed_nodes)
        if not changed:
            return path, traversed_nodes[0]


def LRAT_trial(my_map, start_loc, goal_loc, h_values, traversed_nodes):
    path = []
    x = start_loc
    path.append(x)
    flag = False
    while x != goal_loc:
        y, dummy = look_ahead_update(x, h_values, my_map, traversed_nodes)
        flag = flag or dummy
        path.append(y)
        x = y

    return path, flag


def look_ahead_update(x, h_values, my_map, traversed_nodes):
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
            traversed_nodes[0] += 1
            y = child_loc
            temp = 1 + h_values[child_loc]
    if h_values[x] < 1 + h_values[y]:
        h_values[x] = 1 + h_values[y]
        return y, True
    else:
        return y, False
