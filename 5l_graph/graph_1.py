from copy import deepcopy
from math import inf

def bfs(graph, first_edge):
    visited = [False] * len(graph)
    queue, result = [], []

    queue.append(first_edge)
    visited[first_edge] = True
    while queue:
        current = queue.pop(0)
        result.append(current)
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return result

def dfs(graph, first_edge, visited=None, result=None):
        result = result or []
        visited = visited or [False] * len(graph)
        visited[first_edge] = True
        result.append(first_edge)

        for i in graph[first_edge]:
            if visited[i] == False:
                dfs(graph, i, visited, result)
        return result

def min_weight(distance, visited):
    min = inf
    for i, _ in enumerate(distance):
            if distance[i] < min and not visited[i]:
                min = distance[i]
                min_index = i

    return min_index

def dijkstra(graph, first_edge):

        visited = [False] * len(graph)
        distance = [inf] * len(graph)
        distance[first_edge] = 0

        for cout in range(len(graph)):

            u = min_weight(distance, visited)
            visited[u] = True

            nearest_edges_indices = \
                (i for i, _ in enumerate(graph) if graph[u][i] > 0)

            for v in nearest_edges_indices:

                if not visited[v] and distance[v] > distance[u] + graph[u][v]:
                        distance[v] = distance[u] + graph[u][v]

        return distance


def floyd_warshall(graph):
    distance = deepcopy(graph)
    n = len(distance)

    for i in range(n):
        for j in range(n):
            if i != j and distance[i][j] == 0:
                distance[i][j] = inf

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j],
                                 distance[i][k]+ distance[k][j])
    return distance
