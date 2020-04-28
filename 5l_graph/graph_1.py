

def bfs(graph, start):
    visited = [False] * len(graph)
    queue, result = [], []

    queue.append(start)
    visited[start] = True
    while queue:
        current = queue.pop(0)
        result.append(current)
        for i in graph[current]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return result

def dfs(graph, start, visited=None, result=None):
        result = result or []
        visited = visited or [False] * len(graph)
        visited[start] = True
        result.append(start)

        for i in graph[start]:
            if visited[i] == False:
                dfs(graph, i, visited, result)
        return result
