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
        if constraint['agent'] == agent:
            constraint_table.append(constraint)
        if constraint['agent'] != agent:
            if len(constraint['loc']) == 2:
                con = {'agent': agent, 'loc': [constraint['loc'][1], constraint['loc'][0]],
                       'timestep': constraint['timestep']}
                constraint_table.append(con)
            else:
                con = {'agent': agent, 'loc': [constraint['loc'][0]],
                       'timestep': constraint['timestep']}
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


def new_a_star_MAPF(my_map, start_loc, goal_loc, h_values, agent, constraints):
    closed_list = dict()
    set_list = dict()
    earliest_goal_timestep = 0
    expended_nodes = 0
    generated_nodes = [0]

    # make sure h_values has start_loc
    flag = False
    for h in h_values:
        if h == start_loc:
            flag = True
            break
    if not flag:
        return None, 0, 0  # Failed to find solutions
    constraint_table = build_constraint_table(constraints, agent)
    root = {'loc': start_loc, 'g_val': 0, 'h_val': h_values[start_loc], 'parent': None, 'timestep': 0}
    closed_list[(start_loc, 0)] = h_values[start_loc]
    if len(constraint_table) > 0:
        for cons in constraint_table:
            if cons['timestep'] > earliest_goal_timestep \
                    and cons['loc'] == [goal_loc]:
                earliest_goal_timestep = cons['timestep']

    bound = max(h_values[start_loc], earliest_goal_timestep)
    set_list[bound] = [root]
    expended_nodes += 1
    # result = root
    while True:
        # print(return_set['path'])
        if len(set_list[bound]) == 0:
            # if result['loc'] == goal_loc:
            #     return get_path(result), expended_nodes, generated_nodes[0]
            set_list.pop(bound)
            temp = float("inf")
            for i in set_list:
                if i < temp:
                    temp = i
            bound = temp
        if bound == float("inf"):
            return None, 0, 0
        root = set_list[bound].pop()
        generated_nodes[0] += 1
        # print(return_set['path'])
        root = DeepSearch_MAPF(my_map, bound, h_values, set_list,
                          constraint_table, earliest_goal_timestep, root, closed_list, generated_nodes)
        if root['loc'] == goal_loc:
            return_flag = 0
            for constraint in constraints:
                if constraint['timestep'] >= root['timestep'] and constraint['loc'] == [goal_loc]:
                    return_flag = 1
            if return_flag == 0:
                return get_path(root), expended_nodes, generated_nodes[0]
                # if result['loc'] != goal_loc:
                #     result = root
                # else:
                #     if len(get_path(result)) > len(get_path(root)):
                #         result = root


def DeepSearch_MAPF(my_map, bound, h_values, set_list, constraints, earliest_goal_timestep, node, closed_list, generated_nodes):
    g = node['g_val']
    curr = node['loc']
    open_list = []
    # if h_values[curr] == 0:
    #     return node
    for dir in range(4):
        if dir < 4:
            child_loc = move(curr, dir)
        else:
            child_loc = curr
        if child_loc[0] <= -1 or child_loc[1] <= -1:
            continue
        if child_loc[0] >= len(my_map) or child_loc[1] >= len(my_map[0]):
            continue
        if my_map[child_loc[0]][child_loc[1]]:
            continue

        if is_constrained(curr, child_loc, node['timestep'] + 1, constraints) == 0:
            child = {'loc': child_loc,
                     'g_val': node['g_val'] + 1,
                     'h_val': h_values[child_loc],
                     'parent': node,
                     'timestep': node['timestep'] + 1}
            f = child['g_val'] + child['h_val']
            if f <= bound:
                if (child['loc'], child['timestep']) not in closed_list or closed_list[(child['loc'], child['timestep'])] > f:
                    closed_list[(child['loc'], child['timestep'])] = f
                    new_node = DeepSearch_MAPF(my_map, bound, h_values, set_list, constraints,
                                          earliest_goal_timestep,
                                          child, closed_list, generated_nodes)
                    if new_node['h_val'] == 0:
                        return new_node
            else:
                if (child['loc'], child['timestep']) not in closed_list or closed_list[(child['loc'], child['timestep'])] > f:
                    if (child['loc'], child['timestep']) in closed_list and closed_list[(child['loc'], child['timestep'])] > f:
                        set_list[closed_list[(child['loc'], child['timestep'])]].remove(child.copy())
                    closed_list[(child['loc'], child['timestep'])] = f
                    if f in set_list:
                        set_list[f].append(child.copy())
                        generated_nodes[0] += 1
                    else:
                        set_list[f] = [child.copy()]
                        generated_nodes[0] += 1
    return node