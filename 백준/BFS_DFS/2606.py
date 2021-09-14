from collections import deque
N = int(input())    # 컴퓨터의 수
edge = int(input()) # 네트워크 쌍

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = True
    count = 0
    while q:
        now = q.popleft()
        for x in graph[now]:
            if not visited[x]:
                q.append(x)
                visited[x] = True
                count += 1

    print(count)


bfs(1)

