import sys
import heapq
INF = 987654321
T = int(sys.stdin.readline())

def dijkstra(start, edges, N):
    distance = [INF] * (N+1)
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, d in edges[now]:
            cost = dist + d
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))
    return distance


for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    edges = [[] for _ in range(n+1)]
    problem_edge = 0
    destiny = []
    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        edges[a].append((b, d))
        edges[b].append((a, d))
        if a in (g, h) and b in (g, h):
            problem_edge = d
    for _ in range(t):
        destiny.append(int(sys.stdin.readline()))

    distance_s = dijkstra(s, edges, n)          # s 부터 최단 거리 테이블
    distance_g = dijkstra(g, edges, n)          # g 부터 최단 거리 테이블
    distance_h = dijkstra(h, edges, n)          # h 부터 최단 거리 테이블
    answer = []
    for x in destiny:
        # (s - x) 와 (s - g - h - x) or (s - h - g - x) 비교
        if distance_s[x] == (distance_s[g] + problem_edge + distance_h[x]) or \
            distance_s[x] == (distance_s[h] + problem_edge + distance_g[x]):
            answer.append(x)
    answer.sort()
    for x in answer:
        print(x, end=' ')
    print()


