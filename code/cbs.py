import time as timer
import heapq
from a_star import compute_heuristics, a_star, get_location, get_sum_of_cost
from IDA_table_revision import tt_IDA
from IIDA import IIDA
from learning_real_time_a_star import LRTA_star
from a_star_MAPF import a_star_MAPF
from IIDA_MAPF import IIDA_MAPF


def detect_collision(path1, path2):
    if len(path1) >= len(path2):
        for t in range(len(path1)):
            if t < len(path2):
                if get_location(path1, t) == get_location(path2, t):
                    return {'loc': [get_location(path1, t)], 'timestep': t}
                if get_location(path1, t) == get_location(path2, t - 1) and get_location(path1, t - 1) == get_location(
                        path2, t):
                    return {'loc': [get_location(path1, t - 1), get_location(path1, t)], 'timestep': t}
            else:
                t2 = len(path2) - 1
                if get_location(path1, t) == get_location(path2, t2):
                    return {'loc': [get_location(path1, t)], 'timestep': t}
    else:
        for t in range(len(path2)):
            if t < len(path1):
                if get_location(path1, t) == get_location(path2, t):
                    return {'loc': [get_location(path1, t)], 'timestep': t}
                if get_location(path1, t) == get_location(path2, t - 1) and get_location(path1, t - 1) == get_location(
                        path2, t):
                    return {'loc': [get_location(path1, t - 1), get_location(path1, t)], 'timestep': t}
            else:
                t1 = len(path1) - 1
                if get_location(path1, t1) == get_location(path2, t):
                    return {'loc': [get_location(path2, t)], 'timestep': t}
    return None

    pass


def detect_collisions(paths):
    collisions = []
    for a1 in range(len(paths)):
        temp = a1 + 1
        for a2 in range(temp, len(paths)):
            collision = detect_collision(paths[a1], paths[a2])
            if collision is not None:
                collision_t = {'a1': a1, 'a2': a2, 'loc': collision['loc'], 'timestep': collision['timestep']}
                if not collisions.__contains__(collision_t):
                    collisions.append(collision_t)
    return collisions

    pass


def standard_splitting(collision):
    constraints = []
    if len(collision['loc']) == 1:
        constraint1 = {'agent': collision['a1'], 'loc': [collision['loc'][0]], 'timestep': collision['timestep']}
        constraints.append(constraint1)
        constraint2 = {'agent': collision['a2'], 'loc': [collision['loc'][0]], 'timestep': collision['timestep']}
        constraints.append(constraint2)
    else:
        e_constraint1 = {'agent': collision['a1'], 'loc': [collision['loc'][0], collision['loc'][1]],
                         'timestep': collision['timestep']}
        constraints.append(e_constraint1)
        e_constraint2 = {'agent': collision['a2'], 'loc': [collision['loc'][1], collision['loc'][0]],
                         'timestep': collision['timestep']}
        constraints.append(e_constraint2)
    return constraints

    pass


class CBSSolver(object):

    def __init__(self, my_map, starts, goals):

        self.start_time = None
        self.end_time = None
        self.my_map = my_map
        self.starts = starts
        self.goals = goals
        self.num_of_agents = len(goals)

        self.num_of_generated = 0
        self.num_of_expanded = 0
        self.sum_of_cost = 0
        self.CPU_time = 0

        self.open_list = []

        # compute heuristics for the low-level search
        self.heuristics = []
        for goal in self.goals:
            self.heuristics.append(compute_heuristics(my_map, goal))

    def push_node(self, node):
        heapq.heappush(self.open_list, (node['cost'], len(node['collisions']), self.num_of_generated, node))
        # print("Generate node {}".format(self.num_of_generated))
        self.num_of_generated += 1

    def pop_node(self):
        _, _, id, node = heapq.heappop(self.open_list)
        # print("Expand node {}".format(id))
        self.num_of_expanded += 1
        return node

    def find_solution_a_star(self):

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):
            path = a_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']

    def find_solution_a_star_MAPF(self):

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):
            path = a_star_MAPF(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
                          i, root['constraints'])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        root['collisions'] = detect_collisions(root['paths'])
        self.push_node(root)
        while self.open_list:
            time = timer.time()
            if time - self.start_time > 150:
                self.end_time = timer.time()
                return []
            P = self.pop_node()
            if len(P['collisions']) == 0:
                root = P
                break
            collision = P['collisions'].pop()
            # task 3.3
            constraints = standard_splitting(collision)
            for constraint in constraints:
                Q = {'cost': 0, 'constraints': [constraint], 'paths': [], 'collisions': None}
                for c in P['constraints']:
                    con = c
                    Q['constraints'].append(con)
                for p in P['paths']:
                    Q['paths'].append(p)
                a = constraint['agent']
                path = a_star_MAPF(self.my_map, self.starts[a], self.goals[a], self.heuristics[a], a, Q['constraints'])
                if path is not None:
                    Q['paths'][a] = path
                    Q['collisions'] = detect_collisions(Q['paths'])
                    Q['cost'] = get_sum_of_cost(Q['paths'])
                    self.push_node(Q)

        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']

    def find_solution_LRTA_star(self):

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):
            path = LRTA_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
                          i, root['constraints'])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']

    #
    def find_solution_tt_IDA(self):

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):
            path = tt_IDA(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
                          i, root['constraints'])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']


    def find_solution_IIDA(self):

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path = IIDA(self.my_map, self.starts[i], self.goals[i], self.heuristics[i])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']


    def find_solution_IIDA_MAPF(self):

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path = IIDA_MAPF(self.my_map, self.starts[i], self.goals[i], self.heuristics[i], i, root['constraints'])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        root['collisions'] = detect_collisions(root['paths'])
        self.push_node(root)
        while self.open_list:
            time = timer.time()
            if time - self.start_time > 150:
                self.end_time = timer.time()
                return []
            P = self.pop_node()
            if len(P['collisions']) == 0:
                root = P
                break
            collision = P['collisions'].pop()
            # task 3.3
            constraints = standard_splitting(collision)
            for constraint in constraints:
                Q = {'cost': 0, 'constraints': [constraint], 'paths': [], 'collisions': None}
                for c in P['constraints']:
                    con = c
                    Q['constraints'].append(con)
                for p in P['paths']:
                    Q['paths'].append(p)
                a = constraint['agent']
                path = IIDA_MAPF(self.my_map, self.starts[a], self.goals[a], self.heuristics[a], a, Q['constraints'])
                if path is not None:
                    Q['paths'][a] = path
                    Q['collisions'] = detect_collisions(Q['paths'])
                    Q['cost'] = get_sum_of_cost(Q['paths'])
                    self.push_node(Q)

        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']



    def get_expanded_nodes_MAPF(self):
        return self.num_of_expanded
    def get_generated_nodes_MAPF(self):
        return self.num_of_generated
    def get_cost(self):
        return self.sum_of_cost

    def get_time(self):
        return self.end_time - self.start_time

    def print_results(self, node):
        print("\n Found a solution! \n")
        CPU_time = self.end_time - self.start_time
        print("CPU time (s):    {:.2f}".format(CPU_time))
        print("Sum of costs:    {}".format(get_sum_of_cost(node['paths'])))
        self.sum_of_cost = get_sum_of_cost(node['paths'])
        print("Expanded nodes:  {}".format(self.num_of_expanded))
        print("Generated nodes: {}".format(self.num_of_generated))
        print()
