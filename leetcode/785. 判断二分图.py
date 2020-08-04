import collections

graph = [[1, 3], [0, 2], [1, 3], [0, 2]]


# fixme 对于图中的任意两个节点 uu 和 vv，如果它们之间有一条边直接相连，那么 uu 和 vv 必须属于不同的集合。


def isBipartite(graph):
    n = len(graph)
    UNCOLORED, RED, GREEN = 0, 1, 2
    color = [UNCOLORED] * n
    global valid
    valid = True

    def dfs(node: int, c: int):
        global valid
        color[node] = c
        cNei = (GREEN if c == RED else RED)
        for neighbor in graph[node]:
            if color[neighbor] == UNCOLORED:
                dfs(neighbor, cNei)
                if not valid:
                    return
            elif color[neighbor] != cNei:
                valid = False
                return

    for i in range(n):
        if color[i] == UNCOLORED:
            dfs(i, RED)
            if not valid:
                break

    return valid


def isBipartite_1(graph):
    n = len(graph)
    UNCOLORED, RED, GREEN = 0, 1, 2
    color = [UNCOLORED] * n

    for i in range(n):
        if color[i] == UNCOLORED:
            q = collections.deque([i])
            color[i] = RED
            while q:
                node = q.popleft()
                cNei = (GREEN if color[node] == RED else RED)
                for neighbor in graph[node]:
                    if color[neighbor] == UNCOLORED:
                        q.append(neighbor)
                        color[neighbor] = cNei
                    elif color[neighbor] != cNei:
                        return False

    return True


isBipartite_1(graph)

import queue


def bfs(adj, start):  # 广度优先
    visited = set()
    q = queue.Queue()
    q.put(start)  # 把起始点放入队列
    while not q.empty():
        u = q.get()
        print(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
bfs(graph, 1)


def dfs(adj, start):  # 深度优先
    visited = set()
    stack = [[start, 0]]
    while stack:
        (v, next_child_idx) = stack[-1]
        if (v not in adj) or (next_child_idx >= len(adj[v])):
            stack.pop()
            continue
        next_child = adj[v][next_child_idx]
        stack[-1][1] += 1
        if next_child in visited:
            continue
        print(next_child)
        visited.add(next_child)
        stack.append([next_child, 0])


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
dfs(graph, 1)
