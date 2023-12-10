import heapq
import sys


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


def new_a_star(my_map, start_loc, goal_loc, h_values, agent, constraints):
    sys.setrecursionlimit(1500)
    closed_list = dict()
    set_list = dict()
    earliest_goal_timestep = 0
    expended_nodes = 0
    generated_nodes = [0]
    traversed_nodes = [0]

    # make sure h_values has start_loc
    flag = False
    for h in h_values:
        if h == start_loc:
            flag = True
            break
    if not flag:
        return None, 0, 0, 0  # Failed to find solutions
    # constraint_table = build_constraint_table(constraints, agent)
    constraint_table = []
    root = {'loc': start_loc, 'g_val': 0, 'h_val': h_values[start_loc], 'parent': None}
    closed_list[start_loc] = h_values[start_loc]

    bound = max(h_values[start_loc], earliest_goal_timestep)
    set_list[bound] = [root]
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
            return None, 0, 0, 0
        while len(set_list[bound]) > 0:
            root = set_list[bound].pop()
            expended_nodes += 1
            # print(return_set['path'])
            root = DeepSearch(my_map, bound, h_values, set_list,
                              constraint_table, earliest_goal_timestep, root, closed_list, generated_nodes, traversed_nodes)
            if root['loc'] == goal_loc:
                return get_path(root), expended_nodes, generated_nodes[0], traversed_nodes[0]


def DeepSearch(my_map, bound, h_values, set_list, constraints, earliest_goal_timestep, node, closed_list, generated_nodes, traversed_nodes):
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

        # if is_constrained(curr, child_loc, node['timestep'] + 1, constraints) == 0:
        child = {'loc': child_loc,
                 'g_val': node['g_val'] + 1,
                 'h_val': h_values[child_loc],
                 'parent': node}
        traversed_nodes[0] += 1
        f = child['g_val'] + child['h_val']
        if f <= bound:
            if child['loc'] not in closed_list or closed_list[child['loc']] > f:
                closed_list[child['loc']] = f
                new_node = DeepSearch(my_map, bound, h_values, set_list, constraints,
                                      earliest_goal_timestep,
                                      child, closed_list, generated_nodes, traversed_nodes)
                if new_node['h_val'] == 0:
                    return new_node
        else:
            if child['loc'] not in closed_list or closed_list[child['loc']] > f:
                if child['loc'] in closed_list and closed_list[child['loc']] > f:
                    set_list[closed_list[child['loc']]].remove(child.copy())
                closed_list[child['loc']] = f
                if f in set_list:
                    set_list[f].append(child.copy())
                    generated_nodes[0] += 1
                else:
                    set_list[f] = [child.copy()]
                    generated_nodes[0] += 1
    return node
