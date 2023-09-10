import numpy as np

def move(loc, dir):
    # task 1.1 Add the node that staying at original location
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0), (0, 0)]
    return loc[0] + directions[dir][0], loc[1] + directions[dir][1]

def Q_Learning(my_map, start, goal):
    Q_table = np.ones([len(my_map) + 2, len(my_map[0]) + 2, 5], dtype=float)
    for i in range(len(my_map) * len(my_map[0])):
        curr = {'loc': start, 'parent': None}
        while curr['loc'] != goal and \
                curr['loc'][0] != -1 and \
                curr['loc'][1] != -1 and \
                curr['loc'] != len(my_map) and \
                curr['loc'] != len(my_map[0]) and \
                ( not my_map[curr['loc'][0]][curr['loc'][1]]):
            flag = float('-inf')
            next_dir = 0
            for dir in range(5):
                child = move(curr['loc'], dir)
                Qmax = max(Q_table[child[0] + 1, child[1] + 1, 0:4])
                if curr['loc'] != goal and \
                    curr['loc'][0] != -1 and \
                    curr['loc'][1] != -1 and \
                    curr['loc'] != len(my_map) and \
                    curr['loc'] != len(my_map[0]) and \
                    ( not my_map[curr['loc'][0]][curr['loc'][1]]):
                    Q_table[curr['loc'][0] + 1, curr['loc'][1], dir] = round(Q_table[curr['loc'][0] + 1, curr['loc'][1], dir] + float(0.9) * (float(0.9 * Qmax) - Q_table[curr['loc'][0] + 1, curr['loc'][1] + 1, dir]), 4)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = {'loc': (4, 1), 'g': 3}
    temp = {a['loc'], a['g'] + 1}
    print(temp)
    a = temp
    print(a)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
