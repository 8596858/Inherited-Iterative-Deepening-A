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

def walkable(loc, my_map):
    if loc[0] == -1:
        return False
    if loc[1] == -1:
        return False
    if loc[0] == len(my_map):
        return False
    if loc[1] == len(my_map[0]):
        return False
    if my_map[loc[0]][loc[1]]:
        return False
    return True

def out_of_map(loc, my_map):
    if loc[0] == -1:
        return True
    if loc[1] == -1:
        return True
    if loc[0] == len(my_map):
        return True
    if loc[1] == len(my_map[0]):
        return True
    return False

def jump(curr, my_map, dir, start, goal, timestep, g_value, h_values, agent, constraints, parent):
    M = []
    # 0-left, 1-up, 2-right, 3-down, 4-don't move
    if dir == 1 or dir == 3:
        M.append(0)
        M.append(dir)
        M.append(2)
    if dir == 0 or dir == 2:
        M.append(dir)
    if not walkable(curr, my_map):
        return [parent]
    if is_constrained(parent['loc'], curr, timestep, constraints) == 2:
        temp = [parent]
        return temp
    if dir == 0 or dir == 2:
        if not out_of_map(move(parent['loc'], 1), my_map):
            if my_map[move(parent['loc'], 1)[0]][move(parent['loc'], 1)[1]] and not my_map[move(curr, 1)[0]][move(curr, 1)[1]]\
                    or is_constrained(parent['loc'], move(parent['loc'], 1), timestep, constraints) == 2:
                child = {'loc': curr,
                     'g_val': g_value,
                     'h_val': h_values[curr],
                     'parent': parent,
                     'timestep': timestep}
                return [child]
        if not out_of_map(move(parent['loc'], 3), my_map):
            if my_map[move(parent['loc'], 3)[0]][move(parent['loc'], 3)[1]] and not my_map[move(curr, 3)[0]][move(curr, 3)[1]]\
                    or is_constrained(parent['loc'], move(parent['loc'], 3), timestep, constraints) == 2:
                child = {'loc': curr,
                     'g_val': g_value,
                     'h_val': h_values[curr],
                     'parent': parent,
                     'timestep': timestep}
                return [child]
    if is_constrained(parent['loc'], curr, timestep, constraints) == 1:
        child = {'loc': curr,
                 'g_val': g_value,
                 'h_val': h_values[curr],
                 'parent': parent,
                 'timestep': timestep}
        return [child]
    if curr == goal:
        child = {'loc': curr,
                 'g_val': g_value,
                 'h_val': h_values[curr],
                 'parent': parent,
                 'timestep': timestep}
        return [child]
    S = []
    for d in M:
        child = {'loc': curr,
                 'g_val': g_value,
                 'h_val': h_values[curr],
                 'parent': parent,
                 'timestep': timestep}
        for dic in jump(move(curr, d), my_map, d, start, goal, timestep + 1, g_value + 1, h_values, agent, constraints, child):
            S.append(dic)
    return S

def a_star_JPS(my_map, start_loc, goal_loc, h_values, agent, constraints):
    """ my_map      - binary obstacle map
        start_loc   - start position
        goal_loc    - goal position
        agent       - the agent that is being re-planned
        constraints - constraints defining where robot should or cannot go at each timestep
    """
    open_list = []
    closed_list = dict()
    h_value = h_values[start_loc]
    constraint_table = build_constraint_table(constraints, agent)
    root = {'loc': start_loc, 'g_val': 0, 'h_val': h_value, 'parent': None, 'timestep': 0}

    push_node(open_list, root)
    closed_list[(root['loc']), (root['timestep'])] = root

    while len(open_list) > 0:
        curr = pop_node(open_list)
        if curr['loc'] == goal_loc:
            return_flag = 0
            for constraint in constraint_table:
                if constraint['timestep'] > curr['timestep'] and constraint['loc'] == [goal_loc]:
                    if not constraint['positive']:
                        return_flag = 1
            if return_flag == 0:
                # print(curr)
                return get_path(curr)

        for dir in range(5):
            child_loc = move(curr['loc'], dir)
            timestep = curr['timestep'] + 1
            g_value = curr['g_val'] + 1
            nodes = []
            if not walkable(child_loc, my_map):
                continue
            if is_constrained(curr['loc'], child_loc, curr['timestep'] + 1, constraint_table) == 2:
                continue
            if dir != 4:
                nodes = jump(child_loc, my_map, dir, start_loc, goal_loc, timestep, g_value, h_values, agent,
                         constraint_table, curr)
            # if dir != 4:
                for child in nodes:
                    if (child['loc'], (child['timestep'])) in closed_list:
                        existing_node = closed_list[(child['loc']), (child['timestep'])]
                        if compare_nodes(child, existing_node):
                            closed_list[(child['loc']), (child['timestep'])] = child
                            push_node(open_list, child)
                    else:
                        closed_list[(child['loc']), (child['timestep'])] = child
                        push_node(open_list, child)
            else:
                child = {'loc': child_loc,
                         'g_val': g_value,
                         'h_val': h_values[child_loc],
                         'parent': curr,
                         'timestep': timestep}
                if (child['loc'], (child['timestep'])) in closed_list:
                    existing_node = closed_list[(child['loc']), (child['timestep'])]
                    if compare_nodes(child, existing_node):
                        closed_list[(child['loc']), (child['timestep'])] = child
                        push_node(open_list, child)
                else:
                    closed_list[(child['loc']), (child['timestep'])] = child
                    push_node(open_list, child)

    return None  # Failed to find solutions