import math
import random


def map_generator(size, agent_num, obs_rate, num):
    maps = []
    obs_num = math.ceil(size * size * obs_rate / 100)
    for i in range(num):
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
        for r in range(size):
            my_map.append([])
            for c in range(size):
                my_map[-1].append(False)
        for o in range(obs_num):
            ox = random.randint(0, size - 1)
            oy = random.randint(0, size - 1)
            my_map[ox][oy] = True
        for a in range(agent_num):
            while True:
                sx = random.randint(0, size - 1)
                sy = random.randint(0, size - 1)
                if my_map[sx][sy] is False:
                    start.append((sx, sy))
                    break
            while True:
                ex = random.randint(0, size - 1)
                ey = random.randint(0, size - 1)
                if my_map[ex][ey] is False:
                    end.append((ex, ey))
                    break
        map_dic = {"map": my_map, "start": start, "end": end}
        maps.append(map_dic)

    return maps
