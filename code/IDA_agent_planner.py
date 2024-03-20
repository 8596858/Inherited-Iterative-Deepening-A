import heapq


def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]


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


def push_node(open_list, node):
    heapq.heappush(open_list, (node['g_val'] + node['h_val'], node['h_val'], node['loc'], node))


def pop_node(open_list):
    _, _, _, curr = heapq.heappop(open_list)
    return curr


def compare_nodes(n1, n2):
    """Return true is n1 is better than n2."""
    return n1['g_val'] + n1['h_val'] < n2['g_val'] + n2['h_val']

def get_h_value(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def ID_a_star(my_map, start_loc, goal_loc, h_values):
    open_list = []
    closed_list = dict()
    earliest_goal_timestep = 0

    # make sure h_values has start_loc
    flag = False
    for h in h_values:
        if h == start_loc:
            flag = True
            break
    if not flag:
        return None  # Failed to find solutions

    h_value = h_values[start_loc]
    # constraint_table = build_constraint_table(constraints, agent)
    constraint_table = []
    root = {'loc': start_loc,
            'g_val': 0,
            'h_val': h_value,
            'parent': None}
    open_list.append(root)
    closed_list[(root['loc'], root['g_val'])] = start_loc
    # if len(constraint_table) > 0:
    #     for cons in constraint_table:
    #         if cons['timestep'] > earliest_goal_timestep \
    #                 and cons['loc'] == [goal_loc]:
    #             earliest_goal_timestep = cons['timestep']
    return_set = {'bound': h_value,
                  'node': root,
                  'found': False}
    expended_nodes = 0
    generated_nodes = [0]
    while True:
        # print(returnSet['bound'])
        return_set = DeepSearch(my_map, return_set, h_values,
                                constraint_table, earliest_goal_timestep, closed_list)
        if return_set['found'] is True:
            return get_path(return_set['node'])
        if return_set['bound'] == float("inf"):
            return None


def DeepSearch(my_map, returnSet, h_values, constraints, earliest_goal_timestep, closed_list):
    curr = returnSet['node']
    if h_values[curr['loc']] == 0:
        return {'bound': 0,
                'node': returnSet['node'],
                'found': True}
    new_bound = float("inf")
    for dir in range(4):
        child_loc = move(curr['loc'], dir)
        if child_loc[0] <= -1 or child_loc[1] <= -1:
            continue
        if child_loc[0] >= len(my_map) or child_loc[1] >= len(my_map[0]):
            continue
        if my_map[child_loc[0]][child_loc[1]]:
            continue
        # if is_constrained(curr['loc'], child_loc, curr['timestep'] + 1, constraints) == 0:
        child = {'loc': child_loc,
                 'g_val': curr['g_val'] + 1,
                 'h_val': h_values[child_loc],
                 'parent': curr}
        t_bound = {'bound': returnSet['bound'] - 1,
                   'node': child,
                   'found': False}
        if 1 + child['h_val'] <= returnSet['bound']:
            t_bound = DeepSearch(my_map, t_bound, h_values, constraints, earliest_goal_timestep, closed_list)
            t_bound['bound'] += 1
        else:
            t_bound['bound'] = 1 + child['h_val']
        if 'found' in t_bound and t_bound['found'] is True:
            return t_bound
        new_bound = min(new_bound, t_bound['bound'])
    return {'bound': new_bound,
            'node': curr,
            'found': False}