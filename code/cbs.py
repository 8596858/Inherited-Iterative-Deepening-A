import time as timer
import heapq
import random
from single_agent_planner import compute_heuristics, a_star, get_location, get_sum_of_cost
from JPS_agent_planner import a_star_JPS
from IDA_agent_planner import ID_a_star
from IDA_table_revision import tt_IDA
from new_A_star import new_a_star
from Q_Learning import Q_learning


def detect_collision(path1, path2):
    ##############################
    # Task 3.1: Return the first collision that occurs between two robot paths (or None if there is no collision)
    #           There are two types of collisions: vertex collision and edge collision.
    #           A vertex collision occurs if both robots occupy the same location at the same timestep
    #           An edge collision occurs if the robots swap their location at the same timestep.
    #           You should use "get_location(path, t)" to get the location of a robot at time t.
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
    ##############################
    # Task 3.1: Return a list of first collisions between all robot pairs.
    #           A collision can be represented as dictionary that contains the id of the two robots, the vertex or edge
    #           causing the collision, and the timestep at which the collision occurred.
    #           You should use your detect_collision function to find a collision between two robots.
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
    ##############################
    # Task 3.2: Return a list of (two) constraints to resolve the given collision
    #           Vertex collision: the first constraint prevents the first agent to be at the specified location at the
    #                            specified timestep, and the second constraint prevents the second agent to be at the
    #                            specified location at the specified timestep.
    #           Edge collision: the first constraint prevents the first agent to traverse the specified edge at the
    #                          specified timestep, and the second constraint prevents the second agent to traverse the
    #                          specified edge at the specified timestep
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


def disjoint_splitting(collision):
    ##############################
    # Task 4.1: Return a list of (two) constraints to resolve the given collision
    #           Vertex collision: the first constraint enforces one agent to be at the specified location at the
    #                            specified timestep, and the second constraint prevents the same agent to be at the
    #                            same location at the timestep.
    #           Edge collision: the first constraint enforces one agent to traverse the specified edge at the
    #                          specified timestep, and the second constraint prevents the same agent to traverse the
    #                          specified edge at the specified timestep
    #           Choose the agent randomly
    agent = random.randint(0, 1)
    constraints = []
    if len(collision['loc']) == 1:
        if agent == 0:
            constraint1 = {'agent': collision['a1'], 'loc': [collision['loc'][0]], 'timestep': collision['timestep'],
                           'positive': True}
            constraints.append(constraint1)
            constraint2 = {'agent': collision['a1'], 'loc': [collision['loc'][0]], 'timestep': collision['timestep'],
                           'positive': False}
            constraints.append(constraint2)
        else:
            constraint2 = {'agent': collision['a2'], 'loc': [collision['loc'][0]], 'timestep': collision['timestep'],
                           'positive': True}
            constraints.append(constraint2)
            constraint1 = {'agent': collision['a2'], 'loc': [collision['loc'][0]], 'timestep': collision['timestep'],
                           'positive': False}
            constraints.append(constraint1)
    else:
        if agent == 0:
            e_constraint1 = {'agent': collision['a1'], 'loc': [collision['loc'][0], collision['loc'][1]],
                             'timestep': collision['timestep'], 'positive': True}
            constraints.append(e_constraint1)
            e_constraint2 = {'agent': collision['a1'], 'loc': [collision['loc'][0], collision['loc'][1]],
                             'timestep': collision['timestep'], 'positive': False}
            constraints.append(e_constraint2)
        else:
            e_constraint2 = {'agent': collision['a2'], 'loc': [collision['loc'][1], collision['loc'][0]],
                             'timestep': collision['timestep'], 'positive': True}
            constraints.append(e_constraint2)
            e_constraint1 = {'agent': collision['a2'], 'loc': [collision['loc'][1], collision['loc'][0]],
                             'timestep': collision['timestep'], 'positive': False}
            constraints.append(e_constraint1)
    return constraints

    pass


def paths_violate_constraint(constraint, paths):
    assert constraint['positive'] is True
    rst = []
    for i in range(len(paths)):
        if i == constraint['agent']:
            continue
        curr = get_location(paths[i], constraint['timestep'])
        prev = get_location(paths[i], constraint['timestep'] - 1)
        if len(constraint['loc']) == 1:  # vertex constraint
            if constraint['loc'][0] == curr:
                rst.append(i)
        else:  # edge constraint
            if constraint['loc'][0] == prev or constraint['loc'][1] == curr \
                    or constraint['loc'] == [curr, prev]:
                rst.append(i)
    return rst


class CBSSolver(object):
    """The high-level search of CBS."""

    def __init__(self, my_map, starts, goals):
        """my_map   - list of lists specifying obstacle positions
        starts      - [(x1, y1), (x2, y2), ...] list of start locations
        goals       - [(x1, y1), (x2, y2), ...] list of goal locations
        """

        self.my_map = my_map
        self.starts = starts
        self.goals = goals
        self.num_of_agents = len(goals)

        self.num_of_generated = 0
        self.num_of_expanded = 0
        self.generated_nodes = 0
        self.expanded_nodes = 0
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

    def find_solution(self, disjoint=True):
        """ Finds paths for all agents from their start locations to their goal locations

        disjoint    - use disjoint splitting or not
        """

        self.start_time = timer.time()

        # Generate the root node
        # constraints   - list of constraints
        # paths         - list of paths, one for each agent
        #               [[(x11, y11), (x12, y12), ...], [(x21, y21), (x22, y22), ...], ...]
        # collisions     - list of collisions in paths
        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path, temp1, temp2 = a_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
                          i, root['constraints'])
            self.expanded_nodes += temp1
            self.generated_nodes += temp2
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        root['collisions'] = detect_collisions(root['paths'])
        self.push_node(root)

        # Task 3.1: Testing
        print(root['collisions'])

        # Task 3.2: Testing
        for collision in root['collisions']:
            print(standard_splitting(collision))

        ##############################
        # Task 3.3: High-Level Search
        #           Repeat the following as long as the open list is not empty:
        #             1. Get the next node from the open list (you can use self.pop_node()
        #             2. If this node has no collision, return solution
        #             3. Otherwise, choose the first collision and convert to a list of constraints (using your
        #                standard_splitting function). Add a new child node to your open list for each constraint
        #           Ensure to create a copy of any objects that your child nodes might inherit
        while self.open_list:
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
                path, temp1, temp2 = a_star(self.my_map, self.starts[a], self.goals[a], self.heuristics[a], a, Q['constraints'])
                self.expanded_nodes += temp1
                self.generated_nodes += temp2
                if path is not None:
                    Q['paths'][a] = path
                    Q['collisions'] = detect_collisions(Q['paths'])
                    Q['cost'] = get_sum_of_cost(Q['paths'])
                    self.push_node(Q)

        self.print_results(root)
        return root['paths']

    # def find_solution_JPS(self, disjoint=True):
    #     """ Finds paths for all agents from their start locations to their goal locations
    #
    #     disjoint    - use disjoint splitting or not
    #     """
    #
    #     self.start_time = timer.time()
    #
    #     # Generate the root node
    #     # constraints   - list of constraints
    #     # paths         - list of paths, one for each agent
    #     #               [[(x11, y11), (x12, y12), ...], [(x21, y21), (x22, y22), ...], ...]
    #     # collisions     - list of collisions in paths
    #     root = {'cost': 0,
    #             'constraints': [],
    #             'paths': [],
    #             'collisions': []}
    #     for i in range(self.num_of_agents):  # Find initial path for each agent
    #         path = a_star_JPS(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
    #                       i, root['constraints'])
    #         if path is None:
    #             raise BaseException('No solutions')
    #         root['paths'].append(path)
    #
    #     root['cost'] = get_sum_of_cost(root['paths'])
    #     root['collisions'] = detect_collisions(root['paths'])
    #     self.push_node(root)
    #
    #     # Task 3.1: Testing
    #     print(root['collisions'])
    #
    #     # Task 3.2: Testing
    #     for collision in root['collisions']:
    #         print(standard_splitting(collision))
    #
    #     ##############################
    #     # Task 3.3: High-Level Search
    #     #           Repeat the following as long as the open list is not empty:
    #     #             1. Get the next node from the open list (you can use self.pop_node()
    #     #             2. If this node has no collision, return solution
    #     #             3. Otherwise, choose the first collision and convert to a list of constraints (using your
    #     #                standard_splitting function). Add a new child node to your open list for each constraint
    #     #           Ensure to create a copy of any objects that your child nodes might inherit
    #     while self.open_list:
    #         P = self.pop_node()
    #         if len(P['collisions']) == 0:
    #             root = P
    #             break
    #         collision = P['collisions'].pop()
    #         # task 3.3
    #         constraints = standard_splitting(collision)
    #         for constraint in constraints:
    #             Q = {'cost': 0, 'constraints': [constraint], 'paths': [], 'collisions': None}
    #             for c in P['constraints']:
    #                 con = c
    #                 Q['constraints'].append(con)
    #             for p in P['paths']:
    #                 Q['paths'].append(p)
    #             a = constraint['agent']
    #             path = a_star_JPS(self.my_map, self.starts[a], self.goals[a], self.heuristics[a], a, Q['constraints'])
    #             if path is not None:
    #                 Q['paths'][a] = path
    #                 Q['collisions'] = detect_collisions(Q['paths'])
    #                 Q['cost'] = get_sum_of_cost(Q['paths'])
    #                 self.push_node(Q)
    #
    #     self.print_results(root)
    #     return root['paths']
    #
    # def find_solution_IDA(self, disjoint=True):
    #     """ Finds paths for all agents from their start locations to their goal locations
    #
    #     disjoint    - use disjoint splitting or not
    #     """
    #
    #     self.start_time = timer.time()
    #
    #     # Generate the root node
    #     # constraints   - list of constraints
    #     # paths         - list of paths, one for each agent
    #     #               [[(x11, y11), (x12, y12), ...], [(x21, y21), (x22, y22), ...], ...]
    #     # collisions     - list of collisions in paths
    #     root = {'cost': 0,
    #             'constraints': [],
    #             'paths': [],
    #             'collisions': []}
    #     for i in range(self.num_of_agents):  # Find initial path for each agent
    #         path, temp1, temp2 = ID_a_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
    #                       i, root['constraints'])
    #         self.expanded_nodes += temp1
    #         self.generated_nodes += temp2[0]
    #         if path is None:
    #             raise BaseException('No solutions')
    #         root['paths'].append(path)
    #
    #     root['cost'] = get_sum_of_cost(root['paths'])
    #     root['collisions'] = detect_collisions(root['paths'])
    #     self.push_node(root)
    #
    #     # Task 3.1: Testing
    #     print(root['collisions'])
    #
    #     # Task 3.2: Testing
    #     for collision in root['collisions']:
    #         print(standard_splitting(collision))
    #
    #     ##############################
    #     # Task 3.3: High-Level Search
    #     #           Repeat the following as long as the open list is not empty:
    #     #             1. Get the next node from the open list (you can use self.pop_node()
    #     #             2. If this node has no collision, return solution
    #     #             3. Otherwise, choose the first collision and convert to a list of constraints (using your
    #     #                standard_splitting function). Add a new child node to your open list for each constraint
    #     #           Ensure to create a copy of any objects that your child nodes might inherit
    #     while self.open_list:
    #         P = self.pop_node()
    #         if len(P['collisions']) == 0:
    #             root = P
    #             break
    #         collision = P['collisions'].pop()
    #         # task 3.3
    #         constraints = standard_splitting(collision)
    #         for constraint in constraints:
    #             Q = {'cost': 0, 'constraints': [constraint], 'paths': [], 'collisions': None}
    #             for c in P['constraints']:
    #                 con = c
    #                 Q['constraints'].append(con)
    #             for p in P['paths']:
    #                 Q['paths'].append(p)
    #             a = constraint['agent']
    #             path, temp1, temp2 = ID_a_star(self.my_map, self.starts[a], self.goals[a], self.heuristics[a], a, Q['constraints'])
    #             self.expanded_nodes += temp1
    #             self.generated_nodes += temp2[0]
    #             if path is not None:
    #                 Q['paths'][a] = path
    #                 Q['collisions'] = detect_collisions(Q['paths'])
    #                 Q['cost'] = get_sum_of_cost(Q['paths'])
    #                 self.push_node(Q)
    #
    #     self.print_results(root)
    #     return root['paths']
    #
    # def find_solution_tt_IDA(self, disjoint=True):
    #     """ Finds paths for all agents from their start locations to their goal locations
    #
    #     disjoint    - use disjoint splitting or not
    #     """
    #
    #     self.start_time = timer.time()
    #
    #     # Generate the root node
    #     # constraints   - list of constraints
    #     # paths         - list of paths, one for each agent
    #     #               [[(x11, y11), (x12, y12), ...], [(x21, y21), (x22, y22), ...], ...]
    #     # collisions     - list of collisions in paths
    #     root = {'cost': 0,
    #             'constraints': [],
    #             'paths': [],
    #             'collisions': []}
    #     for i in range(self.num_of_agents):  # Find initial path for each agent
    #         path = tt_IDA(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
    #                       i, root['constraints'])
    #         if path is None:
    #             raise BaseException('No solutions')
    #         root['paths'].append(path)
    #
    #     root['cost'] = get_sum_of_cost(root['paths'])
    #     root['collisions'] = detect_collisions(root['paths'])
    #     self.push_node(root)
    #
    #     # Task 3.1: Testing
    #     print(root['collisions'])
    #
    #     # Task 3.2: Testing
    #     for collision in root['collisions']:
    #         print(standard_splitting(collision))
    #
    #     ##############################
    #     # Task 3.3: High-Level Search
    #     #           Repeat the following as long as the open list is not empty:
    #     #             1. Get the next node from the open list (you can use self.pop_node()
    #     #             2. If this node has no collision, return solution
    #     #             3. Otherwise, choose the first collision and convert to a list of constraints (using your
    #     #                standard_splitting function). Add a new child node to your open list for each constraint
    #     #           Ensure to create a copy of any objects that your child nodes might inherit
    #     while self.open_list:
    #         P = self.pop_node()
    #         if len(P['collisions']) == 0:
    #             root = P
    #             break
    #         collision = P['collisions'].pop()
    #         # task 3.3
    #         constraints = standard_splitting(collision)
    #         for constraint in constraints:
    #             Q = {'cost': 0, 'constraints': [constraint], 'paths': [], 'collisions': None}
    #             for c in P['constraints']:
    #                 con = c
    #                 Q['constraints'].append(con)
    #             for p in P['paths']:
    #                 Q['paths'].append(p)
    #             a = constraint['agent']
    #             path = tt_IDA(self.my_map, self.starts[a], self.goals[a], self.heuristics[a], a, Q['constraints'])
    #             if path is not None:
    #                 Q['paths'][a] = path
    #                 Q['collisions'] = detect_collisions(Q['paths'])
    #                 Q['cost'] = get_sum_of_cost(Q['paths'])
    #                 self.push_node(Q)
    #
    #     self.print_results(root)
    #     return root['paths']

    def find_solution_new_A_star(self, disjoint=True):
        """ Finds paths for all agents from their start locations to their goal locations

        disjoint    - use disjoint splitting or not
        """

        self.start_time = timer.time()

        # Generate the root node
        # constraints   - list of constraints
        # paths         - list of paths, one for each agent
        #               [[(x11, y11), (x12, y12), ...], [(x21, y21), (x22, y22), ...], ...]
        # collisions     - list of collisions in paths
        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path = new_a_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i], i, root['constraints'])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        root['collisions'] = detect_collisions(root['paths'])
        self.push_node(root)

        # Task 3.1: Testing
        print(root['collisions'])

        # Task 3.2: Testing
        for collision in root['collisions']:
            print(standard_splitting(collision))

        ##############################
        # Task 3.3: High-Level Search
        #           Repeat the following as long as the open list is not empty:
        #             1. Get the next node from the open list (you can use self.pop_node()
        #             2. If this node has no collision, return solution
        #             3. Otherwise, choose the first collision and convert to a list of constraints (using your
        #                standard_splitting function). Add a new child node to your open list for each constraint
        #           Ensure to create a copy of any objects that your child nodes might inherit
        while self.open_list:
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
                path = new_a_star(self.my_map, self.starts[a], self.goals[a], self.heuristics[a], a, Q['constraints'])
                if path is not None:
                    Q['paths'][a] = path
                    Q['collisions'] = detect_collisions(Q['paths'])
                    Q['cost'] = get_sum_of_cost(Q['paths'])
                    self.push_node(Q)

        self.print_results(root)
        return root['paths']

    # def find_solution_Q_Learning(self, disjoint=True):
    #     """ Finds paths for all agents from their start locations to their goal locations
    #
    #     disjoint    - use disjoint splitting or not
    #     """
    #
    #     self.start_time = timer.time()
    #
    #     # Generate the root node
    #     # constraints   - list of constraints
    #     # paths         - list of paths, one for each agent
    #     #               [[(x11, y11), (x12, y12), ...], [(x21, y21), (x22, y22), ...], ...]
    #     # collisions     - list of collisions in paths
    #     root = {'cost': 0,
    #             'constraints': [],
    #             'paths': [],
    #             'collisions': []}
    #     for i in range(self.num_of_agents):  # Find initial path for each agent
    #         path = Q_learning(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
    #                       i, root['constraints'])
    #         if path is None:
    #             raise BaseException('No solutions')
    #         root['paths'].append(path)
    #
    #     root['cost'] = get_sum_of_cost(root['paths'])
    #     root['collisions'] = detect_collisions(root['paths'])
    #     self.push_node(root)
    #
    #     # Task 3.1: Testing
    #     print(root['collisions'])
    #
    #     # Task 3.2: Testing
    #     for collision in root['collisions']:
    #         print(standard_splitting(collision))
    #
    #     ##############################
    #     # Task 3.3: High-Level Search
    #     #           Repeat the following as long as the open list is not empty:
    #     #             1. Get the next node from the open list (you can use self.pop_node()
    #     #             2. If this node has no collision, return solution
    #     #             3. Otherwise, choose the first collision and convert to a list of constraints (using your
    #     #                standard_splitting function). Add a new child node to your open list for each constraint
    #     #           Ensure to create a copy of any objects that your child nodes might inherit
    #     while self.open_list:
    #         P = self.pop_node()
    #         if len(P['collisions']) == 0:
    #             root = P
    #             break
    #         collision = P['collisions'].pop()
    #         # task 3.3
    #         constraints = standard_splitting(collision)
    #         for constraint in constraints:
    #             Q = {'cost': 0, 'constraints': [constraint], 'paths': [], 'collisions': None}
    #             for c in P['constraints']:
    #                 con = c
    #                 Q['constraints'].append(con)
    #             for p in P['paths']:
    #                 Q['paths'].append(p)
    #             a = constraint['agent']
    #             path = Q_learning(self.my_map, self.starts[a], self.goals[a], self.heuristics[a], a, Q['constraints'])
    #             if path is not None:
    #                 Q['paths'][a] = path
    #                 Q['collisions'] = detect_collisions(Q['paths'])
    #                 Q['cost'] = get_sum_of_cost(Q['paths'])
    #                 self.push_node(Q)
    #
    #     self.print_results(root)
    #     return root['paths']

    def get_expanded_nodes(self):
        return self.expanded_nodes
    def get_generated_nodes(self):
        return self.generated_nodes
    def get_cost(self):
        return self.sum_of_cost

    def get_time(self):
        return timer.time() - self.start_time

    def print_results(self, node):
        print("\n Found a solution! \n")
        f1 = open("time.txt", 'a')
        f3 = open("expand.txt", 'a')
        CPU_time = timer.time() - self.start_time
        print("CPU time (s):    {:.2f}".format(CPU_time))
        f1.writelines(CPU_time.__str__())
        f1.write('\n')
        print("Sum of costs:    {}".format(get_sum_of_cost(node['paths'])))
        self.sum_of_cost = get_sum_of_cost(node['paths'])
        print("Expanded nodes:  {}".format(self.expanded_nodes))
        f3.writelines(self.expanded_nodes.__str__())
        f3.write('\n')
        print("Generated nodes: {}".format(self.generated_nodes))
        print()
        f1.close()
        f3.close()
