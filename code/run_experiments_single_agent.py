#!/usr/bin/python
import argparse
import tracemalloc
import glob
from pathlib import Path
from single_agent_planner import SingleSolver
from map_generator import map_generator, map_generator_ben
from visualize import Animation

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
            if cell == '@' or cell == 'T':
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
    parser.add_argument('--benchmark', type=str, default=None,
                        help='The name of the benchmark file(s)')
    parser.add_argument('--output_file', type=str, default='map',
                        help='The name of map file')
    parser.add_argument('--self', action='store_true', default=False,
                        help='Generate map')
    parser.add_argument('--test', action='store_true', default=False,
                        help='Make the experiment')

    args = parser.parse_args()

    result_file = open(str(args.instance).rstrip('/*') + ".csv", "w", buffering=1)
    result_file.write(
        "Map file name,A* time (s),fringe time (s),LRTA time (s),TT IDA time (s),IIDA time (s),A* peak memory used,fringe peak memory used,LRTA peak memory "
        "used,TT IDA peak memory used,IIDA peak memory used,A* cost,fringe cost,LRTA cost,TT IDA cost,IIDA cost\n")

    total_time_a_star = 0
    peak_mem_a_star = 0
    sum_of_cost_a_star = 0

    total_time_fringe = 0
    peak_mem_fringe = 0
    sum_of_cost_fringe = 0

    total_time_tt_IDA = 0
    peak_mem_tt_IDA = 0
    sum_of_cost_tt_IDA = 0

    total_time_LRTA = 0
    peak_mem_LRTA = 0
    sum_of_cost_LRTA = 0

    total_time_IIDA = 0
    peak_mem_IIDA = 0
    sum_of_cost_IIDA = 0
    same_cost = 0
    if args.generate_map:
        if args.self:
            size = args.size
            agent_num = args.agent_num
            obs_rate = args.obs_rate
            num = args.map_num
            output = args.output_file
            maps = map_generator(size, agent_num, obs_rate, num, output)
        else:
            agent_num = args.agent_num
            num = args.map_num
            filename = args.benchmark
            output = args.output_file
            maps = map_generator_ben(filename, agent_num, num, output)
    if args.test:
        index = 0
        for file in sorted(glob.glob(args.instance)):

            print("***Import an instance***")
            my_map, starts, goals = import_mapf_instance(file)
            for i in range(starts.__len__()):
                print("{}".format(i) + " {}".format(starts[i]) + " {}".format(goals[i]))
            print("***Run Test***")
            index += 1
            print(index)

            print("***Run IIDA***")
            solver_IIDA = SingleSolver(my_map, starts, goals)
            tracemalloc.start()
            paths_n_ida = solver_IIDA.find_solution_IIDA()
            mem_IIDA = tracemalloc.get_traced_memory()
            print("Memory used: {}".format(mem_IIDA))
            peak_mem_IIDA += mem_IIDA[1]
            tracemalloc.stop()
            total_time_IIDA += solver_IIDA.get_time()
            sum_of_cost_IIDA += solver_IIDA.get_cost()

            print("***Run fringe***")
            solver_fringe = SingleSolver(my_map, starts, goals)
            tracemalloc.start()
            paths_fringe = solver_fringe.find_solution_fringe()
            mem_fringe = tracemalloc.get_traced_memory()
            print("Memory used: {}".format(mem_fringe))
            peak_mem_fringe += mem_fringe[1]
            tracemalloc.stop()
            total_time_fringe += solver_fringe.get_time()
            sum_of_cost_fringe += solver_fringe.get_cost()

            print("***Run A Star***")
            solver_a_star = SingleSolver(my_map, starts, goals)
            tracemalloc.start()
            paths_a_star = solver_a_star.find_solution_a_star()
            mem_a_star = tracemalloc.get_traced_memory()
            print("Memory used: {}".format(mem_a_star))
            peak_mem_a_star += mem_a_star[1]
            tracemalloc.stop()
            total_time_a_star += solver_a_star.get_time()
            sum_of_cost_a_star += solver_a_star.get_cost()

            print("***Run LRTA***")
            solver_LRTA = SingleSolver(my_map, starts, goals)
            tracemalloc.start()
            paths_LRTA = solver_LRTA.find_solution_LRTA_star()
            mem_LRTA = tracemalloc.get_traced_memory()
            print("Memory used: {}".format(mem_LRTA))
            peak_mem_LRTA += mem_LRTA[1]
            tracemalloc.stop()
            total_time_LRTA += solver_LRTA.get_time()
            sum_of_cost_LRTA += solver_LRTA.get_cost()

            print("***Run transposition table IDA***")
            solver_tt_ida = SingleSolver(my_map, starts, goals)
            tracemalloc.start()
            paths_tt_ida = solver_tt_ida.find_solution_tt_IDA()
            mem_tt_IDA = tracemalloc.get_traced_memory()
            print("Memory used: {}".format(mem_tt_IDA))
            peak_mem_tt_IDA += mem_tt_IDA[1]
            tracemalloc.stop()
            total_time_tt_IDA += solver_tt_ida.get_time()
            sum_of_cost_tt_IDA += solver_tt_ida.get_cost()

            if solver_a_star.get_cost() == solver_IIDA.get_cost():
                same_cost += 1
            print()

            # cost = get_sum_of_cost(paths)
            result_file.write("{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format(file,
                                                                                         solver_a_star.get_time(),
                                                                                         solver_fringe.get_time(),
                                                                                         solver_LRTA.get_time(),
                                                                                         solver_tt_ida.get_time(),
                                                                                         solver_IIDA.get_time(),
                                                                                         mem_a_star[1],
                                                                                         mem_fringe[1],
                                                                                         mem_LRTA[1],
                                                                                         mem_tt_IDA[1],
                                                                                         mem_IIDA[1],
                                                                                         solver_a_star.get_cost(),
                                                                                         solver_fringe.get_cost(),
                                                                                         solver_LRTA.get_cost(),
                                                                                         solver_tt_ida.get_cost(),
                                                                                         solver_IIDA.get_cost()))

            if not args.batch:
                print("***Test paths on a simulation***")
                animation = Animation(my_map, starts, goals, paths_n_ida)
                # animation.save("output.mp4", 1.0)
                animation.show()

    print("Total time A*:", total_time_a_star)
    print("Total memory A*:", peak_mem_a_star)
    print("Total cost A*:", sum_of_cost_a_star)
    print("")
    print("Total time fringe:", total_time_fringe)
    print("Total memory fringe:", peak_mem_fringe)
    print("Total cost fringe:", sum_of_cost_fringe)
    print("")
    print("Total time LRTA:", total_time_LRTA)
    print("Total memory LRTA:", peak_mem_LRTA)
    print("Total cost LRTA:", sum_of_cost_LRTA)
    print("")
    print("Total time transposition table IDA:", total_time_tt_IDA)
    print("Total memory transposition table IDA:", peak_mem_tt_IDA)
    print("Total cost transposition table IDA:", sum_of_cost_tt_IDA)
    print("")
    print("Total time IIDA:", total_time_IIDA)
    print("Total memory IIDA:", peak_mem_IIDA)
    print("Total cost IIDA:", sum_of_cost_IIDA)
    print("The same cost:", same_cost)
    result_file.write(
        "{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}\n".format("Sum",
                                                          total_time_a_star,
                                                          total_time_fringe,
                                                          total_time_LRTA,
                                                          total_time_tt_IDA,
                                                          total_time_IIDA,
                                                          peak_mem_a_star,
                                                          peak_mem_fringe,
                                                          peak_mem_LRTA,
                                                          peak_mem_tt_IDA,
                                                          peak_mem_IIDA,
                                                          sum_of_cost_a_star,
                                                          sum_of_cost_fringe,
                                                          sum_of_cost_LRTA,
                                                          sum_of_cost_tt_IDA,
                                                          sum_of_cost_IIDA))
    result_file.close()