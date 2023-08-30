def can_finish(num_tasks, prerequisites):
    graph = [[] for _ in range(num_tasks)]
    visited = [False] * num_tasks
    in_degree = [0] * num_tasks
    start_nodes = []

    for task, dependency in prerequisites:
        graph[dependency].append(task)
        in_degree[task] += 1

    for i in range(num_tasks):
        if in_degree[i] == 0:
            start_nodes.append(i)

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor] or not dfs(neighbor):
                return False
        return True

    for start_node in start_nodes:
        if not visited[start_node]:
            if not dfs(start_node):
                return False

    return True

print(can_finish(4, [[0, 1], [1, 2], [2, 3], [3, 0]]))
print(can_finish(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
print(can_finish(3, [[0, 1], [1, 2], [2, 0]]))
print(can_finish(6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [0, 5]]))
print(can_finish(3, [[1, 0], [2, 1], [0, 2]]))
