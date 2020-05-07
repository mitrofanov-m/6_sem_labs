from graph_1 import *


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def marking(s):
    return bcolors.OKGREEN + s + bcolors.ENDC

def print_g(g_str, result):
    result = list(map(str, result))
    print(result)
    for index, _ in enumerate(result):
        for i in g_str:
            if i in result[:index+1]:
                print(marking(i), end='')
            else:
                print(i, end='')
        print()
    print()

if __name__ == "__main__":
    g_str = '''
        \r 0 -- 1 - 2
        \r |    | /
        \r 3 -- 4 - 5'''

    # use list indexes as names of vertices and lists as nearest neighbors
    graph = [[1, 3],        # 0
             [0, 2, 4],     # 1
             [1, 4],        # 2
             [0, 4],        # 3
             [1, 3, 2, 5],  # 4
             [4]]           # 5
    print('BFS')
    result = bfs(graph, 0)
    print_g(g_str, result)

    print('DFS')
    result = dfs(graph, 0)
    print_g(g_str, result)


    g_str = '''
        \r 0 -(4)- 1 -(1)- 2
        \r |       |     /
        \r(9)     (3) (7)
        \r |       | /
        \r 3 -(1)- 4 -(2)- 5'''

    # use list of lists as matrix
    graph = [[0, 4, 0, 9, 0, 0], # 0
             [4, 0, 1, 0, 3, 0], # 1
             [0, 1, 0, 0, 7, 0], # 2
             [9 ,0, 0, 0, 2, 0], # 3
             [0, 3, 7, 2, 0, 2], # 4
             [0, 0, 0, 0, 2, 0]] # 5

    result = dijkstra(graph, 0)
    print('edge len')
    for i, _ in enumerate(result):
        print(f'{i} -    {result[i]}')

    result = floyd_warshall(graph)
    for distance in result:
        print(distance)


    graph = [(0, 1, 4),
             (0, 3, 9),
             (1, 2, 1),
             (1, 4, 3),
             (2, 4, 7),
             (3, 4, 1),
             (4, 5, 2)]

    print('before:')
    for edge in graph:
        print(edge)

    result = kruskal(graph, nodes_num=6)

    print("mst:")
    for edge in result:
        print(edge)

    
