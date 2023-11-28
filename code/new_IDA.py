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
            if my_map[child_loc[0]][child_loc[1]] == "#":
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

    # # build the heuristics table
    # h_values = dict()
    # for i in range(len(my_map)):
    #     for j in range(len(my_map[0])):
    #         if not my_map[i][j]:
    #             h_values[(i, j)] = abs(i - goal[0]) + abs(j - goal[1])
    # return h_values


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


def sort_nodes(open_list):
    for i in range(len(open_list) - 1):
        for j in range(len(open_list) - i - 1):
            if open_list[j]['f_val'] < open_list[j + 1]['f_val'] or \
                    (open_list[j]['f_val'] == open_list[j + 1]['f_val'] and open_list[j]['h_val'] <= open_list[j + 1]['h_val']):
                temp = open_list[j]
                open_list[j] = open_list[j + 1]
                open_list[j + 1] = temp
    return open_list


def new_IDA(my_map, start_loc, goal_loc, h_values, agent, constraints):
    open_list = []
    closed_list = dict()
    set_list = dict()
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
    constraint_table = build_constraint_table(constraints, agent)
    root = {'loc': start_loc,
            'g_val': 0,
            'h_val': h_value,
            'parent': None,
            'timestep': 0}
    open_list.append(start_loc)
    closed_list[(root['loc'], 0)] = h_value
    if len(constraint_table) > 0:
        for cons in constraint_table:
            if cons['timestep'] > earliest_goal_timestep \
                    and cons['loc'] == [goal_loc]:
                earliest_goal_timestep = cons['timestep']
    return_set = {'bound': h_value,
                  'g_val': 0,
                  'timestep': 0,
                  'closed_list': closed_list,
                  'path': open_list,
                  'found': False}
    check_list = dict()
    check_list[(start_loc)] = h_value
    set_list[h_value] = [return_set]
    lowest_bound = h_value
    expended_nodes = 0
    while True:
        # print(return_set['path'])
        if len(set_list[lowest_bound]) == 0:
            set_list.pop(lowest_bound)
            temp = float("inf")
            for i in set_list:
                if i < temp:
                    temp = i
            lowest_bound = temp
        if lowest_bound == float("inf"):
            return None
        return_set = set_list[lowest_bound].pop()
        # print(return_set['path'])
        return_set = DeepSearch(my_map, return_set, return_set['g_val'], return_set['timestep'], h_values, set_list,
                                constraint_table, earliest_goal_timestep, return_set['path'], closed_list, check_list)
        if return_set['found'] is True:
            return return_set['path'], expended_nodes


def DeepSearch(my_map, returnSet, g, t, h_values, set_list, constraints, earliest_goal_timestep, open_list, closed_list,
               check_list):
    curr = open_list[len(open_list) - 1]
    if h_values[curr] == 0:
        return {'bound': 0,
                'g_val': g,
                'timestep': t,
                'closed_list': closed_list,
                'path': open_list,
                'found': True}
    new_bound = float("inf")
    for dir in range(5):
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

        if is_constrained(curr, child_loc, t + 1, constraints) == 0:
            if g + 1 + h_values[child_loc] <= returnSet['bound']:
                if (child_loc, t + 1) not in closed_list:
                    closed_list[(child_loc, t + 1)] = g + 1 + h_values[child_loc]
                    # closed_list[(child_loc, t + 1)] = child_loc
                    open_list.append(child_loc)
                    t_bound = DeepSearch(my_map, returnSet, g + 1, t + 1, h_values, set_list, constraints,
                                         earliest_goal_timestep,
                                         open_list, closed_list, check_list)
                    if 'found' in t_bound and t_bound['found'] is True:
                        return t_bound
                    new_bound = min(new_bound, t_bound['bound'])
                    # closed_list.pop((child_loc, t + 1))
                    open_list.pop()
                else:
                    if closed_list[(child_loc, t + 1)] > g + 1 + h_values[child_loc]:
                        closed_list[(child_loc, t + 1)] = g + 1 + h_values[child_loc]
                        open_list.append(child_loc)
                        t_bound = DeepSearch(my_map, returnSet, g + 1, t + 1, h_values, set_list, constraints,
                                             earliest_goal_timestep,
                                             open_list, closed_list, check_list)
                        if 'found' in t_bound and t_bound['found'] is True:
                            return t_bound
                        new_bound = min(new_bound, t_bound['bound'])
                        # closed_list.pop((child_loc, t + 1))
                        open_list.pop()
            else:
                f = g + 1 + h_values[child_loc]
                if (child_loc, t + 1) not in closed_list:
                    closed_list[(child_loc, t + 1)] = g + 1 + h_values[child_loc]
                    open_list.append(child_loc)
                    if f in set_list:
                        set_list[f].append(
                            {'bound': f, 'g_val': g, 'timestep': t, 'closed_list': closed_list.copy(),
                             'path': open_list.copy(), 'found': False})
                    else:
                        set_list[f] = [
                            {'bound': f, 'g_val': g, 'timestep': t, 'closed_list': closed_list.copy(),
                             'path': open_list.copy(), 'found': False}]
                    open_list.pop()
                else:
                    if closed_list[(child_loc, t + 1)] > g + 1 + h_values[child_loc]:
                        closed_list[(child_loc, t + 1)] = g + 1 + h_values[child_loc]
                        open_list.append(child_loc)
                        if f in set_list:
                            set_list[f].append(
                                {'bound': f, 'g_val': g, 'timestep': t, 'closed_list': closed_list.copy(),
                                 'path': open_list.copy(), 'found': False})
                        else:
                            set_list[f] = [
                                {'bound': f, 'g_val': g, 'timestep': t, 'closed_list': closed_list.copy(),
                                 'path': open_list.copy(), 'found': False}]
                        open_list.pop()
    return {'bound': new_bound,
            'g_val': g,
            'timestep': t,
            'closed_list': closed_list,
            'path': open_list,
            'found': False}
