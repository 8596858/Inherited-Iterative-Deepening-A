import numpy as np


class MyMap:
    def __init__(self, start, end):
        self.matrix = np.array([['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
                                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                                ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
                                ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']])
        self.edge = 8
        self.start = start
        self.end = end
        if self.matrix[self.start[0], self.start[1]] == '.':
            self.matrix[self.start[0], self.start[1]] = 's'
        if self.matrix[self.end[0], self.end[1]] == '.':
            self.matrix[self.end[0], self.end[1]] = 'e'


def shortestPath(start_loc, end_loc, map):
    xGrouth = (end_loc[0] - start_loc[0]) / abs(end_loc[1] - start_loc[1])
    yGrouth = (end_loc[1] - start_loc[1]) / abs(end_loc[1] - start_loc[1])
    k = (end_loc[1] - start_loc[1]) / (end_loc[0] - start_loc[0])
    d = start_loc[1] - k * start_loc[0]
    path_list = [start_loc]
    currX = start_loc[0]
    if start_loc[0] > end_loc[0]:
        while currX > end_loc[0]:
            currX = currX + xGrouth
            currY = k * currX + d
            path = [round(currX), round(currY)]
            temp = path_list[len(path_list) - 1]
            if path[0] != temp[0] and path[1] != temp[1]:
                if round(currX) < currX:
                    path_list.append([round(currX) + 1, round(currY)])
                else:
                    if start_loc[1] > end_loc[1]:
                        path_list.append([round(currX), round(currY) + 1])
                    else:
                        path_list.append([round(currX), round(currY) - 1])
            path_list.append(path)
    else:
        while currX < end_loc[0]:
            currX = currX + xGrouth
            currY = k * currX + d
            path = [round(currX), round(currY)]
            temp = path_list[len(path_list) - 1]
            if path[0] != temp[0] and path[1] != temp[1]:
                if round(currX) > currX:
                    path_list.append([round(currX) - 1, round(currY)])
                else:
                    if start_loc[1] > end_loc[1]:
                        path_list.append([round(currX), round(currY) + 1])
                    else:
                        path_list.append([round(currX), round(currY) - 1])
            path_list.append(path)
    print(path_list)
    for e in path_list:
        map.matrix[e[0], e[1]] = '@'
    print(map.matrix)


if __name__ == '__main__':
    map = MyMap([5, 9], [1, 1])
    shortestPath([5, 9], [1, 1], map)
