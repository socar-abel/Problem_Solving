from collections import deque
N, K = map(int, input().split())

def bfs(n):
    q = deque()
    q.append((n, 0))
    visit = {n: True}

    while q:
        now, count = q.popleft()

        if now == K: return count

        if 0 <= now + 1 <= 10**6 and not visit.get(now+1):
            visit[now+1] = True
            q.append((now+1, count+1))
        if 0 <= now - 1 <= 10**6 and not visit.get(now-1):
            visit[now-1] = True
            q.append((now-1, count+1))
        if 0 <= now * 2 <= 10**6 and not visit.get(now*2):
            visit[now*2] = True
            q.append((now*2, count+1))


print(bfs(N))
