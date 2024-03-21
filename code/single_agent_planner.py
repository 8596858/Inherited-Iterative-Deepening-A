import time as timer
from a_star import a_star, get_sum_of_cost
from fringe import fringe
from IDA_agent_planner import ID_a_star
from IDA_table_revision import tt_IDA
from IIDA import IIDA
from learning_real_time_a_star import LRTA_star

def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]

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
    h_values = dict()
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if not my_map[i][j]:
                h_values[(i, j)] = abs(i - goal[0]) + abs(j - goal[1])
    return h_values

    # Euclidean distance
    # h_values = dict()
    # for i in range(len(my_map)):
    #     for j in range(len(my_map[0])):
    #         if not my_map[i][j]:
    #             h_values[(i, j)] = int(math.sqrt(math.pow(i - goal[0], 2) + math.pow(j - goal[1], 2)))
    # return h_values

class SingleSolver(object):
    """The high-level search of CBS."""

    def __init__(self, my_map, starts, goals):
        """my_map   - list of lists specifying obstacle positions
        starts      - [(x1, y1), (x2, y2), ...] list of start locations
        goals       - [(x1, y1), (x2, y2), ...] list of goal locations
        """

        self.start_time = None
        self.end_time = None
        self.my_map = my_map
        self.starts = starts
        self.goals = goals
        self.num_of_agents = len(goals)

        self.num_of_generated = 0
        self.num_of_expanded = 0
        self.traversed_nodes = 0
        self.generated_nodes = 0
        self.expanded_nodes = 0
        self.sum_of_cost = 0
        self.CPU_time = 0

        self.open_list = []

        # compute heuristics for the low-level search
        self.heuristics = []
        for goal in self.goals:
            self.heuristics.append(compute_heuristics(my_map, goal))

    def find_solution_a_star(self, disjoint=True):
        """ Finds paths for all agents from their start locations to their goal locations

        disjoint    - use disjoint splitting or not
        """

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path = a_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']

    def find_solution_fringe(self, disjoint=True):
        """ Finds paths for all agents from their start locations to their goal locations

        disjoint    - use disjoint splitting or not
        """

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path = fringe(self.my_map, self.starts[i], self.goals[i], self.heuristics[i])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']

    def find_solution_LRTA_star(self, disjoint=True):
        """ Finds paths for all agents from their start locations to their goal locations

        disjoint    - use disjoint splitting or not
        """

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path = LRTA_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']


    def find_solution_IDA(self, disjoint=True):
        """ Finds paths for all agents from their start locations to their goal locations

        disjoint    - use disjoint splitting or not
        """

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path = ID_a_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']

    #
    def find_solution_tt_IDA(self, disjoint=True):
        """ Finds paths for all agents from their start locations to their goal locations

        disjoint    - use disjoint splitting or not
        """

        self.start_time = timer.time()

        root = {'cost': 0,
                'constraints': [],
                'paths': [],
                'collisions': []}
        for i in range(self.num_of_agents):  # Find initial path for each agent
            path = tt_IDA(self.my_map, self.starts[i], self.goals[i], self.heuristics[i])
            if path is None:
                raise BaseException('No solutions')
            root['paths'].append(path)

        root['cost'] = get_sum_of_cost(root['paths'])
        self.end_time = timer.time()
        self.print_results(root)
        return root['paths']

    def find_solution_IIDA(self, disjoint=True):
        """ Finds paths for all agents from their start locations to their goal locations

        disjoint    - use disjoint splitting or not
        """

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



    def get_expanded_nodes(self):
        return self.expanded_nodes
    def get_generated_nodes(self):
        return self.generated_nodes
    def get_expanded_nodes_MAPF(self):
        return self.num_of_expanded
    def get_generated_nodes_MAPF(self):
        return self.num_of_generated
    def get_traversed_nodes(self):
        return self.traversed_nodes
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
