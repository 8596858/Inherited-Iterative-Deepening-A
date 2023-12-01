import math
import random
import heapq

def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]

def map_generator(size, agent_num, obs_rate, num):
    maps = []
    obs_num = math.ceil(size * size * obs_rate / 100)
    for i in range(num):
        while True:
            my_map = []
            start = []
            end = []
            # for r in range(size):
            #     my_map.append([])
            #     for c in range(size):
            #         r = random.randint(1, 100)
            #         if r > obs_rate:
            #             my_map[-1].append(False)
            #         else:
            #             my_map[-1].append(True)
            # for r in range(size):
            #     my_map.append([])
            #     for c in range(size):
            #         my_map[-1].append(False)
            # for o in range(obs_num):
            #     ox = random.randint(0, size - 1)
            #     oy = random.randint(0, size - 1)
            #     my_map[ox][oy] = True
            for r in range(size):
                my_map.append([])
                for c in range(size):
                    my_map[-1].append(False)
            temp = int((size - 1) / 2)
            for x in range(temp):
                for y in range(temp):
                    my_map[x * 2 + 1][y * 2 + 1] = True
            for a in range(agent_num):
                flag = True
                while flag:
                    sx = random.randint(0, size - 1)
                    sy = random.randint(0, size - 1)
                    if my_map[sx][sy] is False and start.__contains__((sx, sy)) is False:
                        start.append((sx, sy))
                        flag = False
                flag = True
                while flag:
                    ex = random.randint(0, size - 1)
                    ey = random.randint(0, size - 1)
                    if my_map[ex][ey] is False and end.__contains__((ex, ey)) is False:
                        end.append((ex, ey))
                        flag = False
            flag = True
            for s in range(start.__len__()):
                h_values = compute_heuristics(my_map, end[s])
                if h_values.__contains__(start[s]) is False:
                    flag = False
                    break
            if flag is True:
                map_dic = {"map": my_map, "start": start, "end": end}
                maps.append(map_dic)
                f = open("map/" + str(i) + ".txt", "w")
                f.write(str(size) + " " + str(size) + "\n")
                for x in range(size):
                    for y in range(size):
                        if my_map[x][y] is False:
                            f.write(". ")
                        else:
                            f.write("@ ")
                    f.write("\n")
                f.write(str(agent_num) + "\n")
                for a in range(agent_num):
                    f.write(str(start[a][0]) + " " + str(start[a][1]) + " " + str(end[a][0]) + " " + str(end[a][1]) + "\n")
                f.close()
                break

    return maps

def compute_heuristics(my_map, goal):
    # Use Dijkstra to build a shortest-path tree rooted at the goal location
    open_list = []
    closed_list = dict()
    root = {'loc': goal, 'cost': 0}
    heapq.heappush(open_list, (root['cost'], goal, root))
    closed_list[goal] = root
    while len(open_list) > 0:
        (cost, loc, curr) = heapq.heappop(open_list)
        for dir in range(4):
            child_loc = move(loc, dir)
            child_cost = cost + 1
            if child_loc[0] < 0 or child_loc[0] >= len(my_map) \
                    or child_loc[1] < 0 or child_loc[1] >= len(my_map[0]):
                continue
            if my_map[child_loc[0]][child_loc[1]]:
                continue
            child = {'loc': child_loc, 'cost': child_cost}
            if child_loc in closed_list:
                existing_node = closed_list[child_loc]
                if existing_node['cost'] > child_cost:
                    closed_list[child_loc] = child
                    # open_list.delete((existing_node['cost'], existing_node['loc'], existing_node))
                    heapq.heappush(open_list, (child_cost, child_loc, child))
            else:
                closed_list[child_loc] = child
                heapq.heappush(open_list, (child_cost, child_loc, child))

    # build the heuristics table
    h_values = dict()
    for loc, node in closed_list.items():
        h_values[loc] = node['cost']
    return h_values
