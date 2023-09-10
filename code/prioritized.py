import time as timer
from single_agent_planner import compute_heuristics, a_star, get_sum_of_cost


class PrioritizedPlanningSolver(object):
    """A planner that plans for each robot sequentially."""

    def __init__(self, my_map, starts, goals):
        """my_map   - list of lists specifying obstacle positions
        starts      - [(x1, y1), (x2, y2), ...] list of start locations
        goals       - [(x1, y1), (x2, y2), ...] list of goal locations
        """

        self.my_map = my_map
        self.starts = starts
        self.goals = goals
        self.num_of_agents = len(goals)

        self.CPU_time = 0

        # compute heuristics for the low-level search
        self.heuristics = []
        for goal in self.goals:
            self.heuristics.append(compute_heuristics(my_map, goal))

    def find_solution(self):
        """ Finds paths for all agents from their start locations to their goal locations."""

        start_time = timer.time()
        result = []
        constraints = []
        # constraint = {'agent': 0, 'loc': [(1, 5)], 'timestep': 4}
        # constraints.append(constraint)
        # constraint = {'agent': 1, 'loc': [(1, 2), (1, 3)], 'timestep': 1}
        # constraints.append(constraint)
        # constraint = {'agent': 0, 'loc': [(1, 5)], 'timestep': 10}
        # constraints.append(constraint)
        # constraint = {'agent': 1, 'loc': [(1, 4)], 'timestep': 2}
        # constraints.append(constraint)
        # constraint = {'agent': 1, 'loc': [(1, 3), (1, 2)], 'timestep': 2}
        # constraints.append(constraint)
        # constraint = {'agent': 1, 'loc': [(1, 3)], 'timestep': 2}
        # constraints.append(constraint)
        # constraint = {'agent': 1, 'loc': [(1, 2)], 'timestep': 1}
        # constraints.append(constraint)

        for i in range(self.num_of_agents):  # Find path for each agent
            path = a_star(self.my_map, self.starts[i], self.goals[i], self.heuristics[i],
                          i, constraints)
            if path is None:
                raise BaseException('No solutions')
            result.append(path)

            ##############################
            # Task 2: Add constraints here
            #         Useful variables:
            #            * path contains the solution path of the current (i'th) agent, e.g., [(1,1),(1,2),(1,3)]
            #            * self.num_of_agents has the number of total agents
            #            * constraints: array of constraints to consider for future A* searches
            for index in range(self.num_of_agents):
                if index != i:
                    for timestep in range(len(path)):
                        # task 2.1
                        constraint = {'agent': index, 'loc': [path[timestep]], 'timestep': timestep}
                        constraints.append(constraint)
                        # task 2.2
                        if timestep > 0:
                            constraint = {'agent': index, 'loc': [path[timestep], path[timestep - 1]], 'timestep': timestep}
                            constraints.append(constraint)
                            constraint = {'agent': index, 'loc': [path[timestep - 1], path[timestep]], 'timestep': timestep}
                            constraints.append(constraint)
            #         print("1")
            #         print(constraints)

                    # task 2.3
                    path_index = a_star(self.my_map, self.starts[index], self.goals[index], self.heuristics[index],
                                        index, constraints)
                    if path_index is None:
                        raise BaseException('No solutions')
                        return None
                    if len(path_index) > len(path):
                        check = 1
                        while check == 1:
                            path_index = a_star(self.my_map, self.starts[index], self.goals[index], self.heuristics[index],
                                        index, constraints)

                            # task 2.4
                            length = 0
                            for path_r in result:
                                length = len(path_r) + length
                            if path_index is None or len(path_index) > (length + len(self.my_map) * len(self.my_map[0])) * 4:
                                raise BaseException('No solutions')
                                return None

                            # task 2.3
                            check = 0
                            for timestep in range(len(path), len(path_index)):
                                if path_index[timestep] == path[len(path) - 1]:
                                    constraint = {'agent': index, 'loc': [path[len(path) - 1]], 'timestep': timestep}
                                    if not constraints.__contains__(constraint):
                                        constraints.append(constraint)
                                    constraint = {'agent': index, 'loc': [path_index[timestep], path_index[timestep - 1]],
                                                  'timestep': timestep}
                                    if not constraints.__contains__(constraint):
                                        constraints.append(constraint)
                                    constraint = {'agent': index,
                                                  'loc': [path_index[timestep - 1], path_index[timestep]],
                                                  'timestep': timestep}
                                    if not constraints.__contains__(constraint):
                                        constraints.append(constraint)
                                    check = 1
            ##############################

        self.CPU_time = timer.time() - start_time

        print("\n Found a solution! \n")
        print("CPU time (s):    {:.2f}".format(self.CPU_time))
        print("Sum of costs:    {}".format(get_sum_of_cost(result)))
        print(result)
        return result
