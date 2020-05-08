from graph_1 import dfs

def _matrix2lists(graph):
    n = len(graph)
    result = [list() for i in range(n)]
    for i, vertex in enumerate(graph):
        for j, _ in enumerate(vertex):
            if vertex[j] == 1:
                result[i].append(j)

    return result

def _correct_euler(graph):
    n = len(graph)
    odd_vertices_num = 0

    # check of euler rules
    for i in range(0, n):
        if sum(graph[i]) % 2 == 1:
            odd_vertices_num += 1

    if odd_vertices_num > 2:
        print("Error: Too many odd vertices")
        return False

    tmp_graph = _matrix2lists(graph)
    if len(dfs(tmp_graph, 0)) < len(graph):
        print("Error: More than 1 component")
        return False

    return True

def _euler_path_of(graph, current, result):
    nearest_edges_indices = \
        (i for i, _ in enumerate(graph) if graph[current][i] > 0)
    for next in nearest_edges_indices:
        graph[current][next] = 0
        graph[next][current] = 0
        _euler_path_of(graph, next, result)
    result.append(current)

def euler(graph):
    if not _correct_euler(graph):
        return None

    first_vertex = 0
    for i in range(len(graph)):
        if sum(graph[i]) % 2 == 1:
            first_vertex = i
            break

    result = []
    _euler_path_of(graph, first_vertex, result)

    return result


# --------------------------------

def _correct_edge(u, v):
    pass

def _fleury_path_of(graph, current, result):
    nearest_edges_indices = \
        (i for i, _ in enumerate(graph) if graph[current][i] > 0)
    for next in nearest_edges_indices:
        if _correct_edge(current, next):
            result.append(next)
            graph[current][next] = 0
            graph[next][current] = 0
            _fleury_path_of(graph, next, result)


def fleury(self):
    first_vertex = 0
    for i in range(len(graph)):
        if sum(graph[i]) % 2 == 1:
            first_vertex = i
            break

    result = []
    _fleury_path_of(graph, first_vertex, result)



if __name__ == '__main__':
    graph_1 = [[0, 1, 0, 0, 1],
               [1, 0, 1, 1, 1],
               [0, 1, 0, 1, 0],
               [0, 1, 1, 0, 0],
               [1, 1, 0, 0, 0]]

    graph_2 = [[0, 1, 0, 1, 1],
               [1, 0, 1, 0, 1],
               [0, 1, 0, 1, 1],
               [1, 1, 1, 0, 0],
               [1, 0, 1, 0, 0]]

    print(euler(graph_1))
    print(euler(graph_2))
