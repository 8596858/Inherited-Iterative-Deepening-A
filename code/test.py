if __name__ == '__main__':
    a_list = []
    node1 = {'1': 1, '2': 2, '3': 3, '4': 4}
    node3 = {'1': 1, '2': 2, '3': 3, '4': 4}
    node2 = {'1': 5, '2': 6, '3': 7, '4': 8}
    a_list.append(node1)
    a_list.append(node2)
    print(a_list)
    a_list.remove(node3)
    print(a_list)