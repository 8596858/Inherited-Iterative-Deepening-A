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

def get_h_value(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# def ID_a_star(my_map, start_loc, goal_loc, h_values, agent, constraints):
#     closed_list = dict()
#     h_value = get_h_value(start_loc, goal_loc)
#     constraint_table = build_constraint_table(constraints, agent)
#     root = {'loc': start_loc, 'g_val': 0, 'h_val': h_value, 'parent': None, 'timestep': 0}
#     closed_list[root['loc']] = root
#     earliest_goal_timestep = 0
#     expended_nodes = 0
#     if len(constraint_table) > 0:
#         for cons in constraint_table:
#             if cons['timestep'] > earliest_goal_timestep \
#                     and cons['loc'] == [goal_loc]:
#                 earliest_goal_timestep = cons['timestep']
#     # up_bound = max(min(start_loc[0], goal_loc[0]) - 1, 0)
#     # down_bound = min(max(start_loc[0], goal_loc[0]) + 1, len(my_map) - 1)
#     # left_bound = max(min(start_loc[1], goal_loc[1]) - 1, 0)
#     # right_bound = min(max(start_loc[1], goal_loc[1]) + 1, len(my_map[0]) - 1)
#     path, expended_nodes = deep_limit_search(my_map, goal_loc, h_values, constraint_table, root, closed_list, expended_nodes,
#                              earliest_goal_timestep)
#     # print(path)
#     return path, expended_nodes, 0
#
#
# def deep_limit_search(my_map, goal_loc, h_values, constraint_table, node, closed_list, expended_nodes,
#                       earliest_goal_timestep):
#     open_list = []
#     up_bound = round(max(min(node['loc'][0], goal_loc[0]) - 2, -1))
#     down_bound = round(min(max(node['loc'][0], goal_loc[0]) + 2, len(my_map)))
#     left_bound = round(max(min(node['loc'][1], goal_loc[1]) - 2, -1))
#     right_bound = round(min(max(node['loc'][1], goal_loc[1]) + 2, len(my_map[0])))
#     if node['loc'] == goal_loc:
#         return_flag = 0
#         for constraint in constraint_table:
#             if constraint['timestep'] > node['timestep'] and constraint['loc'] == [goal_loc]:
#                 if not constraint['positive']:
#                     return_flag = 1
#         if return_flag == 0:
#             return get_path(node), expended_nodes
#
#     for dir in range(5):
#         child_loc = move(node['loc'], dir)
#         if child_loc[0] == up_bound:
#             continue
#         if child_loc[1] == left_bound:
#             continue
#         if child_loc[0] == down_bound:
#             continue
#         if child_loc[1] == right_bound:
#             continue
#         if my_map[child_loc[0]][child_loc[1]]:
#             continue
#
#         if is_constrained(node['loc'], child_loc, node['timestep'] + 1, constraint_table) == 0:
#
#             child = {'loc': child_loc,
#                      'g_val': node['g_val'] + 1,
#                      'h_val': get_h_value(child_loc, goal_loc),
#                      'parent': node,
#                      'timestep': node['timestep'] + 1}
#
#             if child['loc'] in closed_list:
#                 existing_node = closed_list[child['loc']]
#                 if compare_nodes(child, existing_node):
#                     closed_list[child['loc']] = child
#                     push_node(open_list, child)
#             else:
#                 closed_list[child['loc']] = child
#                 push_node(open_list, child)
#     while len(open_list) > 0:
#         curr = pop_node(open_list)
#         expended_nodes = expended_nodes + 1
#         path, temp = deep_limit_search(my_map, goal_loc, h_values, constraint_table, curr, closed_list,
#                                                        expended_nodes,
#                                                        earliest_goal_timestep)
#         if path is not None:
#             return path, temp
#
#         if curr['loc'] == goal_loc:
#             return_flag = 0
#             for constraint in constraint_table:
#                 if constraint['timestep'] > curr['timestep'] and constraint['loc'] == [goal_loc]:
#                     if not constraint['positive']:
#                         return_flag = 1
#             if return_flag == 0:
#                 return get_path(curr), expended_nodes
#
#         for dir in range(5):
#             child_loc = move(curr['loc'], dir)
#             if child_loc[0] == up_bound:
#                 continue
#             if child_loc[1] == left_bound:
#                 continue
#             if child_loc[0] == down_bound:
#                 continue
#             if child_loc[1] == right_bound:
#                 continue
#             if my_map[child_loc[0]][child_loc[1]]:
#                 continue
#
#             if is_constrained(curr['loc'], child_loc, curr['timestep'] + 1, constraint_table) == 0:
#
#                 child = {'loc': child_loc,
#                          'g_val': curr['g_val'] + 1,
#                          'h_val': get_h_value(child_loc, goal_loc),
#                          'parent': curr,
#                          'timestep': curr['timestep'] + 1}
#
#                 if child['loc'] in closed_list:
#                     existing_node = closed_list[child['loc']]
#                     if compare_nodes(child, existing_node):
#                         closed_list[child['loc']] = child
#                         push_node(open_list, child)
#                 else:
#                     closed_list[child['loc']] = child
#                     push_node(open_list, child)
#
#     return None, 0  # Failed to find solutions


def ID_a_star(my_map, start_loc, goal_loc, h_values, agent, constraints):
    pre_open_list = []
    sub_open_list = []
    closed_list = dict()
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
        return None  # Failed to find solutions

    h_value = get_h_value(start_loc, goal_loc)
    constraint_table = build_constraint_table(constraints, agent)
    root = {'loc': start_loc,
            'g_val': 0,
            'h_val': h_value,
            'parent': None,
            'timestep': 0}
    push_node(pre_open_list, root)
    generated_nodes[0] += 1
    closed_list[(root['loc'], root['timestep'])] = root
    if len(constraint_table) > 0:
        for cons in constraint_table:
            if cons['timestep'] > earliest_goal_timestep \
                    and cons['loc'] == [goal_loc]:
                earliest_goal_timestep = cons['timestep']
    bound = h_value
    while True:
        curr = {'loc': None,
                'g_val': 0,
                'h_val': 0,
                'parent': None,
                'timestep': 0}
        if len(pre_open_list) > 0:
            curr = pop_node(pre_open_list)
            # print(len(pre_open_list))
            expended_nodes += 1
            if curr['loc'] == goal_loc:
                return_flag = 0
                for constraint in constraint_table:
                    if constraint['timestep'] > curr['timestep'] and constraint['loc'] == [goal_loc]:
                        if not constraint['positive']:
                            return_flag = 1
                if return_flag == 0:
                    return get_path(curr), expended_nodes, generated_nodes

        DeepSearch(my_map, curr, h_values, constraint_table, earliest_goal_timestep, bound, pre_open_list, sub_open_list, closed_list, generated_nodes, goal_loc)
        # for dir in range(5):
        #     child_loc = move(curr['loc'], dir)
        #     if child_loc[0] == -1:
        #         continue
        #     if child_loc[1] == -1:
        #         continue
        #     if child_loc[0] == len(my_map):
        #         continue
        #     if child_loc[1] == len(my_map[0]):
        #         continue
        #     if my_map[child_loc[0]][child_loc[1]]:
        #         continue
        #
        #     if is_constrained(curr['loc'], child_loc, curr['timestep'] + 1, constraint_table) == 0:
        #         child = {'loc': child_loc,
        #                 'g_val': curr['g_val'] + 1,
        #                 'h_val': get_h_value(child_loc, goal_loc),
        #                 'parent': curr,
        #                 'timestep': curr['timestep'] + 1}
        #         if child['g_val'] + child['h_val'] <= bound:
        #             if (child['loc'], (child['timestep'])) in closed_list:
        #                 existing_node = closed_list[(child['loc']), (child['timestep'])]
        #                 if compare_nodes(child, existing_node):
        #                     closed_list[(child['loc']), (child['timestep'])] = child
        #                     push_node(pre_open_list, child)
        #                     generated_nodes += 1
        #             else:
        #                 closed_list[(child['loc']), (child['timestep'])] = child
        #                 push_node(pre_open_list, child)
        #                 generated_nodes += 1
        #         else:
        #             if (child['loc'], (child['timestep'])) in closed_list:
        #                 existing_node = closed_list[(child['loc']), (child['timestep'])]
        #                 if compare_nodes(child, existing_node):
        #                     closed_list[(child['loc']), (child['timestep'])] = child
        #                     push_node(sub_open_list, child)
        #                     generated_nodes += 1
        #             else:
        #                 closed_list[(child['loc']), (child['timestep'])] = child
        #                 push_node(sub_open_list, child)
        #                 generated_nodes += 1
        #
        if len(pre_open_list) == 0:
            pre_open_list = sub_open_list
            # print(len(pre_open_list))
            sub_open_list = []
            # print(len(sub_open_list))
            bound += 1
        # if bound['found']:
        #     path = get_path(bound['node'])
        #     return path, expended_nodes, generated_nodes


def DeepSearch(my_map, node, h_values, constraints, earliest_goal_timestep, bound, pre_open_list, sub_open_list, closed_list, generated_nodes, goal_loc):
    for dir in range(5):
        child_loc = move(node['loc'], dir)
        if child_loc[0] <= -1 or child_loc[1] <= -1:
            continue
        if child_loc[0] >= len(my_map) or child_loc[1] >= len(my_map[0]):
            continue
        if my_map[child_loc[0]][child_loc[1]]:
            continue
        if is_constrained(node['loc'], child_loc, node['timestep'] + 1, constraints) == 0:
            child = {'loc': child_loc,
                     'g_val': node['g_val'] + 1,
                     'h_val': get_h_value(child_loc, goal_loc),
                     'parent': node,
                     'timestep': node['timestep'] + 1}
            # if child_loc == goal_loc:
            #     return child
            if child['g_val'] + child['h_val'] <= bound:
                if (child['loc'], (child['timestep'])) in closed_list:
                    existing_node = closed_list[(child['loc']), (child['timestep'])]
                    if compare_nodes(child, existing_node):
                        closed_list[(child['loc']), (child['timestep'])] = child
                        push_node(pre_open_list, child)
                        generated_nodes[0] += 1
                else:
                    closed_list[(child['loc']), (child['timestep'])] = child
                    push_node(pre_open_list, child)
                    generated_nodes[0] += 1
            else:
                if (child['loc'], (child['timestep'])) in closed_list:
                    existing_node = closed_list[(child['loc']), (child['timestep'])]
                    if compare_nodes(child, existing_node):
                        closed_list[(child['loc']), (child['timestep'])] = child
                        push_node(sub_open_list, child)
                        generated_nodes[0] += 1
                else:
                    closed_list[(child['loc']), (child['timestep'])] = child
                    push_node(sub_open_list, child)
                    generated_nodes[0] += 1

