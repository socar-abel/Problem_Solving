from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
maxWeight = 0
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    maxWeight = max(maxWeight, C)

start, end = map(int, sys.stdin.readline().split())


# w 무게를 가지고 배송이 가능한지
def isPossible(w):
    result = False
    visit = [False] * (N+1)
    q = deque()
    q.append(start)
    visit[start] = True

    while q:
        now = q.popleft()
        if now == end:
            result = True
            break
        for node, cost in graph[now]:
            if not visit[node] and cost >= w:
                q.append(node)
                visit[node] = True
    return result


# 무게를 가지고 이분탐색
left = 0
right = maxWeight
answer = 0

while left <= right:
    mid = (left + right) // 2
    possible = isPossible(mid)

    if possible:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
