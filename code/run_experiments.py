#!/usr/bin/python
import argparse
import tracemalloc
import glob
from pathlib import Path
from cbs import CBSSolver
from map_generator import map_generator
from independent import IndependentSolver
from prioritized import PrioritizedPlanningSolver
from visualize import Animation
from single_agent_planner import get_sum_of_cost

SOLVER = "CBS"

def print_mapf_instance(my_map, starts, goals):
    print('Start locations')
    print_locations(my_map, starts)
    print('Goal locations')
    print_locations(my_map, goals)


def print_locations(my_map, locations):
    starts_map = [[-1 for _ in range(len(my_map[0]))] for _ in range(len(my_map))]
    for i in range(len(locations)):
        starts_map[locations[i][0]][locations[i][1]] = i
    to_print = ''
    for x in range(len(my_map)):
        for y in range(len(my_map[0])):
            if starts_map[x][y] >= 0:
                to_print += str(starts_map[x][y]) + ' '
            elif my_map[x][y]:
                to_print += '@ '
            else:
                to_print += '. '
        to_print += '\n'
    print(to_print)


def import_mapf_instance(filename):
    f = Path(filename)
    if not f.is_file():
        raise BaseException(filename + " does not exist.")
    f = open(filename, 'r')
    # first line: #rows #columns
    line = f.readline()
    rows, columns = [int(x) for x in line.split(' ')]
    rows = int(rows)
    columns = int(columns)
    # #rows lines with the map
    my_map = []
    for r in range(rows):
        line = f.readline()
        my_map.append([])
        for cell in line:
            if cell == '@':
                my_map[-1].append(True)
            elif cell == '.':
                my_map[-1].append(False)
    # #agents
    line = f.readline()
    num_agents = int(line)
    # #agents lines with the start/goal positions
    starts = []
    goals = []
    for a in range(num_agents):
        line = f.readline()
        sx, sy, gx, gy = [int(x) for x in line.split(' ')]
        starts.append((sx, sy))
        goals.append((gx, gy))
    f.close()
    return my_map, starts, goals


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Runs various MAPF algorithms')
    parser.add_argument('--instance', type=str, default=None,
                        help='The name of the instance file(s)')
    parser.add_argument('--batch', action='store_true', default=False,
                        help='Use batch output instead of animation')
    parser.add_argument('--disjoint', action='store_true', default=False,
                        help='Use the disjoint splitting')
    parser.add_argument('--solver', type=str, default=SOLVER,
                        help='The solver to use (one of: {CBS,Independent,Prioritized}), defaults to ' + str(SOLVER))
    parser.add_argument('--size', type=int, default=10,
                        help='The size of the map')
    parser.add_argument('--agent_num', type=int, default=1,
                        help='The num of the agents')
    parser.add_argument('--obs_rate', type=int, default=0,
                        help='The num of obstacles')
    parser.add_argument('--map_num', type=int, default=1,
                        help='The num of the map')
    parser.add_argument('--generate_map', action='store_true', default=False,
                        help='Generate map')
    parser.add_argument('--test', action='store_true', default=False,
                        help='Make the experiment')

    args = parser.parse_args()


    result_file = open("results.csv", "w", buffering=1)
    result_file.write("Map file name, A* time (s), New IDA time (s), A* expended nodes, New IDA expended nodes, A* generated nodes, New IDA generated nodes, A* memory used, New IDA memory used, A* cost, New IDA cost\n")

    # num_of_nodes = 0
    # total_time = 0
    num_of_nodes_a_star = 0
    num_of_g_nodes_a_star = 0
    total_time_a_star = 0
    total_mem_a_star = 0
    sum_of_cost_a_star = 0
    num_of_nodes_JPS = 0
    total_time_JPS = 0
    sum_of_cost_JPS = 0
    num_of_nodes_IDA = 0
    total_time_IDA = 0
    num_of_nodes_n_IDA = 0
    num_of_g_nodes_n_IDA = 0
    total_time_n_IDA = 0
    total_mem_n_IDA = 0
    sum_of_cost_n_IDA = 0
    same_cost = 0
    if args.generate_map:
        size = args.size
        agent_num = args.agent_num
        obs_rate = args.obs_rate
        num = args.map_num
        maps = map_generator(size,agent_num,obs_rate, num)
    if args.test:
        index = 0
        for file in sorted(glob.glob(args.instance)):

            print("***Import an instance***")
            my_map, starts, goals = import_mapf_instance(file)
            # print_mapf_instance(my_map, starts, goals)
        # for m in maps:
            # if args.solver == "CBS":
            #     print("***Run CBS***")
            #     cbs = CBSSolver(m["map"], m["start"], m["end"])
            #     paths = cbs.find_solution(args.disjoint)
            #     num_of_nodes += cbs.get_expanded_nodes()
            #     total_time += cbs.get_time()
            # elif args.solver == "JPS":
            #     print("***Run Independent***")
            #     cbs = CBSSolver(m["map"], m["start"], m["end"])
            #     paths = cbs.find_solution_JPS(args.disjoint)
            #     num_of_nodes += cbs.get_expanded_nodes()
            #     total_time += cbs.get_time()
            # elif args.solver == "IDA":
            #     print("***Run Prioritized***")
            #     cbs = CBSSolver(m["map"], m["start"], m["end"])
            #     paths = cbs.find_solution_IDA(args.disjoint)
            #     num_of_nodes += cbs.get_expanded_nodes()
            #     total_time += cbs.get_time()
            # elif args.solver == "tt_IDA":
            #     print("***Run Prioritized***")
            #     cbs = CBSSolver(m["map"], m["start"], m["end"])
            #     paths = cbs.find_solution_tt_IDA(args.disjoint)
            #     num_of_nodes += cbs.get_expanded_nodes()
            #     total_time += cbs.get_time()
            # elif args.solver == "Q_Learning":
            #     print("***Run Prioritized***")
            #     cbs = CBSSolver(m["map"], m["start"], m["end"])
            #     paths = cbs.find_solution_Q_Learning(args.disjoint)
            #     num_of_nodes += cbs.get_expanded_nodes()
            #     total_time += cbs.get_time()
            # elif args.solver == "Independent":
            #     print("***Run Independent***")
            #     solver = IndependentSolver(m["map"], m["start"], m["end"])
            #     paths = solver.find_solution()
            # elif args.solver == "Prioritized":
            #     print("***Run Prioritized***")
            #     solver = PrioritizedPlanningSolver(m["map"], m["start"], m["end"])
            #     paths = solver.find_solution()
            # if args.solver == "CBS":
            #     print_mapf_instance(my_map, starts, goals)
            #     print("***Run CBS***")
            #     print("***Run A Star***")
            #     cbs_a_star = CBSSolver(my_map, starts, goals)
            #     paths_a_star = cbs_a_star.find_solution(args.disjoint)
            #     num_of_nodes_a_star += cbs_a_star.get_expanded_nodes()
            #     total_time_a_star += cbs_a_star.get_time()
            #     print()
            #     print("***Run IDA***")
            #     cbs_ida = CBSSolver(my_map, starts, goals)
            #     paths_IDA = cbs_ida.find_solution_IDA(args.disjoint)
            #     num_of_nodes_IDA += cbs_ida.get_expanded_nodes()
            #     total_time_IDA += cbs_ida.get_time()
            if args.solver == "CBS":
                # print_mapf_instance(my_map, starts, goals)
                for i in range(starts.__len__()):
                    print("{}".format(i) + " {}".format(starts[i]) + " {}".format(goals[i]))
                print("***Run CBS***")
                index += 1
                print(index)
                print("***Run A Star***")
                tracemalloc.start()
                cbs_a_star = CBSSolver(my_map, starts, goals)
                paths_a_star = cbs_a_star.find_solution(args.disjoint)
                mem_a_star = tracemalloc.get_traced_memory()
                print("Memory used: {}".format(mem_a_star))
                total_mem_a_star += mem_a_star[0]
                tracemalloc.stop()
                num_of_nodes_a_star += cbs_a_star.get_expanded_nodes()
                num_of_g_nodes_a_star += cbs_a_star.get_generated_nodes()
                total_time_a_star += cbs_a_star.get_time()
                sum_of_cost_a_star += cbs_a_star.get_cost()
                # print("***Run JPS***")
                # cbs_jps = CBSSolver(m["map"], m["start"], m["end"])
                # paths_jps = cbs_jps.find_solution_JPS(args.disjoint)
                # # num_of_nodes_JPS += cbs_jps.get_expanded_nodes()
                # sum_of_cost_JPS += cbs_jps.get_cost()
                # total_time_JPS += cbs_jps.get_time()
                # print("***Run IDA***")
                # cbs_ida = CBSSolver(m["map"], m["start"], m["end"])
                # paths_ida = cbs_ida.find_solution_tt_IDA(args.disjoint)
                # num_of_nodes_IDA += cbs_ida.get_expanded_nodes()
                # total_time_IDA += cbs_ida.get_time()
                print("***Run new IDA***")
                tracemalloc.start()
                cbs_n_ida = CBSSolver(my_map, starts, goals)
                paths_n_ida = cbs_n_ida.find_solution_new_A_star(args.disjoint)
                mem_n_IDA = tracemalloc.get_traced_memory()
                print("Memory used: {}".format(mem_n_IDA))
                total_mem_n_IDA += mem_n_IDA[0]
                tracemalloc.stop()
                num_of_nodes_n_IDA += cbs_n_ida.get_expanded_nodes()
                num_of_g_nodes_n_IDA += cbs_n_ida.get_generated_nodes()
                total_time_n_IDA += cbs_n_ida.get_time()
                sum_of_cost_n_IDA += cbs_n_ida.get_cost()
                if cbs_a_star.get_cost() == cbs_n_ida.get_cost():
                    same_cost += 1
                print()
            else:
                raise RuntimeError("Unknown solver!")

            # cost = get_sum_of_cost(paths)
            result_file.write("{},{},{},{},{},{},{},{},{},{},{}\n".format(file, cbs_a_star.get_time(), cbs_n_ida.get_time(),
                                                                    cbs_a_star.get_expanded_nodes(),
                                                                    cbs_n_ida.get_expanded_nodes(),
                                                                    cbs_a_star.get_generated_nodes(),
                                                                    cbs_n_ida.get_generated_nodes(), mem_a_star[0],
                                                                    mem_n_IDA[0], cbs_a_star.get_cost(),
                                                                    cbs_n_ida.get_cost()))


            if not args.batch:
                print("***Test paths on a simulation***")
                animation = Animation(my_map, starts, goals, paths_n_ida)
                # animation.save("output.mp4", 1.0)
                animation.show()
    print("Total expanded nodes A star:", num_of_nodes_a_star)
    print("Total generated nodes A star:", num_of_g_nodes_a_star)
    print("Total time A star:", total_time_a_star)
    print("Total memory A star:", total_mem_a_star)
    print("Total cost A star:", sum_of_cost_a_star)
    # print("Total expanded nodes JPS:", num_of_nodes_JPS)
    # print("Total time JPS:", total_time_JPS)
    # print("Total cost JPS:", sum_of_cost_JPS)
    # print("Total expanded nodes IDA:", num_of_nodes_IDA)
    # print("Total time IDA:", total_time_IDA)
    print("Total expanded nodes new IDA:", num_of_nodes_n_IDA)
    print("Total generated nodes new IDA:", num_of_g_nodes_n_IDA)
    print("Total time new IDA:", total_time_n_IDA)
    print("Total memory new IDA:", total_mem_n_IDA)
    print("Total cost new IDA:", sum_of_cost_n_IDA)
    print("The same cost:", same_cost)
    result_file.write("{},{},{},{},{},{},{},{},{},{},{}\n".format("Sum", total_time_a_star, total_time_n_IDA,
                                                            num_of_nodes_a_star,
                                                            num_of_nodes_n_IDA,
                                                            num_of_g_nodes_a_star,
                                                            num_of_g_nodes_n_IDA, total_mem_a_star,
                                                            sum_of_cost_n_IDA, sum_of_cost_a_star, sum_of_cost_n_IDA))
    result_file.close()
