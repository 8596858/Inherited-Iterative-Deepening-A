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
