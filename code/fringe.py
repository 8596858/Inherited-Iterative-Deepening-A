import heapq
import math


def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]


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

def fringe(my_map, start_loc, goal_loc, h_values):
    F = []
    C = dict()

    h_value = h_values[start_loc]
    flimit = h_value
    root = {'loc': start_loc, 'g_val': 0, 'h_val': h_value, 'parent': None}
    # push_node(F, root)
    F.append(root)
    C[root['loc']] = root
    found = False
    while not found and len(F) > 0:
        fmin = float('inf')
        index = 0
        while index < len(F):
            curr = F[index]
            f = curr['g_val'] + curr['h_val']
            if f > flimit:
                index += 1
                fmin = min(f, fmin)
                continue
        # curr = pop_node(F)

        # task 4
            if curr['loc'] == goal_loc:
                found = True
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
                child = {'loc': child_loc,
                         'g_val': curr['g_val'] + 1,
                         'h_val': h_values[child_loc],
                         'parent': curr}

                if child_loc in C:
                    existing_node = C[child_loc]
                    if child['g_val'] >= existing_node['g_val']:
                        continue
                if child in F:
                    F.remove(child)
                F.append(child)
                C[child['loc']] = child
            F.remove(curr)
        flimit = fmin

    return None  # Failed to find solutions
