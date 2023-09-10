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


def ID_a_star(my_map, start_loc, goal_loc, h_values, agent, constraints):
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
    constraint_table = build_constraint_table(constraints, agent)
    root = {'loc': start_loc,
            'g_val': 0,
            'h_val': h_value,
            'parent': None,
            'timestep': 0}
    push_node(open_list, root)
    closed_list[(root['loc'], root['timestep'])] = root
    if len(constraint_table) > 0:
        for cons in constraint_table:
            if cons['timestep'] > earliest_goal_timestep \
                    and cons['loc'] == [goal_loc]:
                earliest_goal_timestep = cons['timestep']
    num = 0
    bound = {'node': root,
             'bound': h_value,
             'found': False}
    while True:
        if len(open_list) > 0:
            node = pop_node(open_list)
            bound = {'node': node,
                     'bound': h_values[node['loc']],
                     'found': False}
        bound = DeepSearch(my_map, bound, h_values, constraint_table, earliest_goal_timestep, open_list, closed_list)
        num += 1
        if bound['found']:
            path = get_path(bound['node'])
            return path


def DeepSearch(my_map, bound, h_values, constraints, earliest_goal_timestep, open_list, closed_list):
    if h_values[bound['node']['loc']] == 0 and bound['node']['timestep'] >= earliest_goal_timestep:
        return {'node': bound['node'],
                'bound': 0,
                'found': True}
    new_bound = float("inf")
    for dir in range(5):
        if dir < 4:
            child_loc = move(bound['node']['loc'], dir)
        else:
            child_loc = bound['node']['loc']
        if child_loc[0] <= -1 or child_loc[1] <= -1:
            continue
        if child_loc[0] >= len(my_map) or child_loc[1] >= len(my_map[0]):
            continue
        if my_map[child_loc[0]][child_loc[1]]:
            continue
        child = {'loc': child_loc,
                 'g_val': bound['node']['g_val'] + 1,
                 'h_val': h_values[child_loc],
                 'parent': bound['node'],
                 'timestep': bound['node']['timestep'] + 1}
        if is_constrained(bound['node']['loc'], child['loc'], child['timestep'], constraints) == 0:
            b = -1
            t_bound = dict()
            if 1 + child['h_val'] <= bound['bound']:
                temp = {'node': child,
                        'bound': bound['bound'] - 1,
                        'found': False}
                t_bound = DeepSearch(my_map, temp, h_values, constraints, earliest_goal_timestep, open_list, closed_list)
                b = 1 + t_bound['bound']
            else:
                b = 1 + child['h_val']
                if (child['loc'], child['timestep']) not in closed_list:
                    closed_list[(child['loc'], child['timestep'])] = child
                    push_node(open_list, child)
            if 'found' in t_bound and t_bound['found']:
                return {'node': t_bound['node'],
                        'bound': b,
                        'found': t_bound['found']}
            new_bound = min(new_bound, b)
    return {'node': bound['node'],
            'bound': new_bound,
            'found': False}