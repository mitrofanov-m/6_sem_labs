
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
    # use list indexes as names of vertices
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
