import heapq
import math


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
    #         if my_map[child_loc[0]][child_loc[1]]:
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

    # Manhattan
    # h_values = dict()
    # for i in range(len(my_map)):
    #     for j in range(len(my_map[0])):
    #         if not my_map[i][j]:
    #             h_values[(i, j)] = abs(i - goal[0]) + abs(j - goal[1])
    # return h_values

    # Euclidean distance
    h_values = dict()
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if not my_map[i][j]:
                h_values[(i, j)] = int(math.sqrt(math.pow(i - goal[0], 2) + math.pow(j - goal[1], 2)))
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

def get_h_value(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def a_star(my_map, start_loc, goal_loc, h_values):
    open_list = []
    closed_list = dict()

    h_value = h_values[start_loc]
    root = {'loc': start_loc, 'g_val': 0, 'h_val': h_value, 'parent': None}
    push_node(open_list, root)
    closed_list[root['loc']] = root['g_val'] + root['h_val']
    while len(open_list) > 0:
        curr = pop_node(open_list)

        # task 4
        if curr['loc'] == goal_loc:
            return get_path(curr)

        for dir in range(4):
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

            if child_loc in closed_list:
                existing_node = closed_list[child_loc]
                if curr['g_val'] + 1 + h_values[child_loc] < closed_list[child_loc]:
                    child = {'loc': child_loc,
                             'g_val': curr['g_val'] + 1,
                             'h_val': h_values[child_loc],
                             'parent': curr}
                    closed_list[child['loc']] = child['g_val'] + child['h_val']
                    push_node(open_list, child)
            else:
                child = {'loc': child_loc,
                         'g_val': curr['g_val'] + 1,
                         'h_val': h_values[child_loc],
                         'parent': curr}
                closed_list[child['loc']] = child['g_val'] + child['h_val']
                push_node(open_list, child)

    return None  # Failed to find solutions