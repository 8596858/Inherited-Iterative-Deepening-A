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


def compute_heuristics(my_map, goal):
    # Use Dijkstra to build a shortest-path tree rooted at the goal location
    # open_list = []
    # closed_list = dict()
    # root = {'loc': goal, 'cost': 0}
    # heapq.heappush(open_list, (root['cost'], goal, root))
    # closed_list[goal] = root
    # while len(open_list) > 0:
    #     (cost, loc, curr) = heapq.heappop(open_list)
    #     for dir in range(4):
    #         child_loc = move(loc, dir)
    #         child_cost = cost + 1
    #         if child_loc[0] < 0 or child_loc[0] >= len(my_map) \
    #                 or child_loc[1] < 0 or child_loc[1] >= len(my_map[0]):
    #             continue
    #         if my_map[child_loc[0]][child_loc[1]] == "#":
    #             continue
    #         child = {'loc': child_loc, 'cost': child_cost}
    #         if child_loc in closed_list:
    #             existing_node = closed_list[child_loc]
    #             if existing_node['cost'] > child_cost:
    #                 closed_list[child_loc] = child
    #                 # open_list.delete((existing_node['cost'], existing_node['loc'], existing_node))
    #                 heapq.heappush(open_list, (child_cost, child_loc, child))
    #         else:
    #             closed_list[child_loc] = child
    #             heapq.heappush(open_list, (child_cost, child_loc, child))
    #
    # # build the heuristics table
    # h_values = dict()
    # for loc, node in closed_list.items():
    #     h_values[loc] = node['cost']
    # return h_values
    h_values = dict()
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if not my_map[i][j]:
                h_values[(i, j)] = abs(i - goal[0]) + abs(j - goal[1])
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


def sort_sets(set_list):
    for i in range(len(set_list) - 1):
        for j in range(len(set_list) - i - 1):
            if set_list[j]['bound'] < set_list[j + 1]['bound']:
                temp = set_list[j]
                set_list[j] = set_list[j + 1]
                set_list[j + 1] = temp
    return set_list


def new_a_star(my_map, start_loc, goal_loc, h_values, agent, constraints):
    h_value = h_values[start_loc]
    constraint_table = build_constraint_table(constraints, agent)
    root = {'loc': start_loc, 'g_val': 0, 'h_val': h_value, 'root': None, 'parent': None, 'timestep': 0}
    set_list = []
    earliest_goal_timestep = 0
    expended_nodes = 0
    if len(constraint_table) > 0:
        for cons in constraint_table:
            if cons['timestep'] > earliest_goal_timestep \
                    and cons['loc'] == [goal_loc]:
                earliest_goal_timestep = cons['timestep']

    return_set = {'bound': h_value,
                  'node': root,
                  'found': False}
    set_list.append(return_set)
    check_list = dict()
    check_list[root['loc']] = return_set
    while True:
        # root_list = dict()
        # sort_sets(set_list)
        # return_set = set_list.pop()
        # closed_list = dict()
        # closed_list[return_set['node']['loc']] = return_set['node']
        # print(return_set['node']['loc'], " ", return_set['bound'])
        # path, expended_nodes, return_set = deep_limit_search(my_map, goal_loc, closed_list, set_list, check_list, return_set, h_values, constraint_table, return_set['node'],
        #                                          root_list, expended_nodes, earliest_goal_timestep)
        # if path is not None:
        #     print(path)
        #     return path, expended_nodes
        # elif return_set['bound'] == float("inf"):
        #     return None

        root_list = dict()
        closed_list = dict()
        closed_list[(root['loc'], root['timestep'])] = root
        path, expended_nodes, return_set = deep_limit_search(my_map, goal_loc, closed_list, set_list, check_list,
                                                             return_set, h_values, constraint_table, root,
                                                             root_list, expended_nodes, earliest_goal_timestep)
        if path is not None:
            print(path)
            return path
        elif return_set['bound'] == float("inf"):
            return None


def deep_limit_search(my_map, goal_loc, closed_list, set_list, check_list, return_set, h_values, constraint_table, node, root_list, expended_nodes,
                      earliest_goal_timestep):
    open_list = []
    up_bound = round(max(min(node['loc'][0], goal_loc[0]) - 2, -1))
    down_bound = round(min(max(node['loc'][0], goal_loc[0]) + 2, len(my_map)))
    left_bound = round(max(min(node['loc'][1], goal_loc[1]) - 2, -1))
    right_bound = round(min(max(node['loc'][1], goal_loc[1]) + 2, len(my_map[0])))
    push_node(open_list, node)
    new_bound = float("inf")

    while len(open_list) > 0:
        curr = pop_node(open_list)
        expended_nodes = expended_nodes + 1

        if curr['g_val'] + curr['h_val'] > return_set['bound']:
            # if curr['root']['loc'] in check_list:
            #     if check_list[curr['root']['loc']]['bound'] > curr['g_val'] + curr['h_val']:
            #         check_list[curr['root']['loc']] = {'bound': curr['g_val'] + curr['h_val'], 'node': curr['root'], 'found': False}
            #         set_list.append({'bound': curr['g_val'] + curr['h_val'], 'node': curr['root'], 'found': False})
            # else:
            #     set_list.append({'bound': curr['g_val'] + curr['h_val'], 'node': curr['root'], 'found': False})
            return None, expended_nodes, {'bound': curr['g_val'] + curr['h_val'], 'node': curr['root'], 'found': False}

        if curr['loc'] == goal_loc:
            return_flag = 0
            for constraint in constraint_table:
                if constraint['timestep'] > curr['timestep'] and constraint['loc'] == [goal_loc]:
                    if not constraint['positive']:
                        return_flag = 1
            if return_flag == 0:
                return get_path(curr), expended_nodes, {'bound': 0, 'node': curr['root'], 'found': True}

        if (curr['loc'], (curr['timestep'])) not in root_list:
            root_list[(curr['loc']), (curr['timestep'])] = curr
            path, temp, temp_set = deep_limit_search(my_map, goal_loc, closed_list, set_list, check_list, return_set, h_values, constraint_table, curr, root_list,
                                           expended_nodes, earliest_goal_timestep)
            if path is not None:
                return path, temp, {'bound': 0, 'node': curr['root'], 'found': True}
            new_bound = min(new_bound, temp_set['bound'])
        else:
            existing_node = root_list[(curr['loc']), (curr['timestep'])]
            if compare_nodes(curr, existing_node):
                root_list[(curr['loc']), (curr['timestep'])] = curr
                path, temp, temp_set = deep_limit_search(my_map, goal_loc, closed_list, set_list, check_list, return_set,
                                                         h_values, constraint_table, curr, root_list,
                                                         expended_nodes, earliest_goal_timestep)
                if path is not None:
                    return path, temp, {'bound': 0, 'node': curr['root'], 'found': True}
                new_bound = min(new_bound, temp_set['bound'])

        for dir in range(5):
            child_loc = move(curr['loc'], dir)
            if child_loc[0] == up_bound:
                continue
            if child_loc[1] == left_bound:
                continue
            if child_loc[0] == down_bound:
                continue
            if child_loc[1] == right_bound:
                continue
            if my_map[child_loc[0]][child_loc[1]]:
                continue

            if is_constrained(curr['loc'], child_loc, curr['timestep'] + 1, constraint_table) == 0:

                child = {'loc': child_loc,
                         'g_val': curr['g_val'] + 1,
                         'h_val': h_values[child_loc],
                         'root': node,
                         'parent': curr,
                         'timestep': curr['timestep'] + 1}

                if (child['loc'], (child['timestep'])) in closed_list:
                    existing_node = closed_list[(child['loc']), (child['timestep'])]
                    if compare_nodes(child, existing_node):
                        closed_list[(child['loc']), (child['timestep'])] = child
                        push_node(open_list, child)
                else:
                    closed_list[(child['loc']), (child['timestep'])] = child
                    push_node(open_list, child)

    return None, 0, {'bound': new_bound, 'node': node['root'],  'found': False}  # Failed to find solutions
