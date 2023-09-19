#!/usr/bin/python
import argparse
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

    args = parser.parse_args()


    result_file = open("results.csv", "w", buffering=1)

    # num_of_nodes = 0
    # total_time = 0
    num_of_nodes_a_star = 0
    total_time_a_star = 0
    num_of_nodes_IDA = 0
    total_time_IDA = 0
    # for file in sorted(glob.glob(args.instance)):
    #
    #     print("***Import an instance***")
    #     my_map, starts, goals = import_mapf_instance(file)
    #     print_mapf_instance(my_map, starts, goals)
    size = args.size
    agent_num = args.agent_num
    obs_rate = args.obs_rate
    num = args.map_num
    maps = map_generator(size,agent_num,obs_rate, num)
    for m in maps:
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
            print_mapf_instance(m["map"], m["start"], m["end"])
            for i in range(m["start"].__len__()):
                print("{}".format(i) + " {}".format(m["start"][i]) + " {}".format(m["end"][i]))
            print("***Run CBS***")
            print("***Run TT IDA***")
            cbs_a_star = CBSSolver(m["map"], m["start"], m["end"])
            paths_a_star = cbs_a_star.find_solution_tt_IDA(args.disjoint)
            num_of_nodes_a_star += cbs_a_star.get_expanded_nodes()
            total_time_a_star += cbs_a_star.get_time()
            print()
            print("***Run IDA***")
            cbs_ida = CBSSolver(m["map"], m["start"], m["end"])
            paths_IDA = cbs_ida.find_solution_IDA(args.disjoint)
            num_of_nodes_IDA += cbs_ida.get_expanded_nodes()
            total_time_IDA += cbs_ida.get_time()
        else:
            raise RuntimeError("Unknown solver!")

        # cost = get_sum_of_cost(paths)
        # result_file.write("{},{}\n".format(file, cost))


        if not args.batch:
            print("***Test paths on a simulation***")
            animation = Animation(m["map"], m["start"], m["end"])
            # animation.save("output.mp4", 1.0)
            animation.show()
    print("Total expanded nodes TT i:", num_of_nodes_a_star)
    print("Total time A star:", total_time_a_star)
    print("Total expanded nodes IDA:", num_of_nodes_IDA)
    print("Total time: IDA", total_time_IDA)
    result_file.close()
