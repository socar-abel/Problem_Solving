import sys
T = int(sys.stdin.readline())
answer = []

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    answer.append(N-1)

for a in answer:
    print(a)
