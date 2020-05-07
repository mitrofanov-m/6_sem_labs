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

    print('--------------- Graph search algorithms ---------------------- ')

    print('1. BFS')
    result = bfs(graph, 0)
    print_g(g_str, result)

    print('2. DFS')
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
             [9 ,0, 0, 0, 1, 0], # 3
             [0, 3, 7, 1, 0, 2], # 4
             [0, 0, 0, 0, 2, 0]] # 5

    print()
    print('--------------- Shortest path problem ---------------------- ')
    print(g_str)
    result = dijkstra(graph, 0)
    print('\n1. Dijkstra:')
    print('0 - ', result)
    print()

    result = floyd_warshall(graph)
    print('\n2. Floyd Warshall:')
    for i, distance in enumerate(result):
        print(i, ' - ', distance)
    print()


    print('--------------- Minimum Spanning Tree ---------------------- ')
    graph1 = [(0, 1, 4),
             (0, 3, 9),
             (1, 2, 1),
             (1, 4, 3),
             (2, 4, 7),
             (3, 4, 1),
             (4, 5, 2)]



    print('before:')
    print(g_str, end='\n\n')
    for edge in graph1:
        print(edge)

    result = prim_mst(graph)
    print('\n1. Prim:')
    for edge in result:
        print(edge)

    result = kruskal_mst(graph1, nodes_num=6)

    print("\n2. Kruskal:")
    for edge in result:
        print(edge)
