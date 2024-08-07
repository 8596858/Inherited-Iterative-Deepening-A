import heapq


def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]



def build_constraint_table(constraints, agent):
    constraint_table = []

    # task 4
    for constraint in constraints:
        if constraint['agent'] == agent:
            constraint_table.append(constraint)

    return constraint_table
    pass


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


def a_star_MAPF(my_map, start_loc, goal_loc, h_values, agent, constraints):
    open_list = []
    closed_list = dict()

    h_value = h_values[start_loc]
    constraint_table = build_constraint_table(constraints, agent)
    root = {'loc': start_loc, 'g_val': 0, 'h_val': h_value, 'parent': None, 'timestep': 0}
    push_node(open_list, root)
    closed_list[(root['loc']), (root['timestep'])] = root
    while len(open_list) > 0:
        curr = pop_node(open_list)

        # task 4
        if curr['loc'] == goal_loc:
            return_flag = 0
            for constraint in constraint_table:
                if constraint['timestep'] > curr['timestep'] and constraint['loc'] == [goal_loc]:
                    return_flag = 1
            if return_flag == 0:
                return get_path(curr)

        for dir in range(5):
            child_loc = move(curr['loc'], dir)
            if child_loc[0] == -1:
                continue
            if child_loc[1] == -1:
                continue
            if child_loc[0] == len(my_map):
                continue
            if child_loc[1] == len(my_map[0]):
                continue
            if my_map[child_loc[0]][child_loc[1]]:
                continue

            if is_constrained(curr['loc'], child_loc, curr['timestep'] + 1, constraint_table) == 0:
                child = {'loc': child_loc,
                        'g_val': curr['g_val'] + 1,
                        'h_val': h_values[child_loc],
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

    return None  # Failed to find solutions