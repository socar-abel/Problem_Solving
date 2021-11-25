import sys
from collections import deque
S = int(sys.stdin.readline())
dp = [[-1]*(2*S+1) for _ in range(2*S+1)]

q = deque()
# 노드, 클립보드 수, 연산 수
q.append((1, 0, 0))
dp[1][0] = 0

while q:
    node, clipboard, cnt = q.popleft()

    # 클립보드에 복사, 무한 복사는 일어나지 않도록 함
    if 0 <= node <= 2*S and dp[node][node] == -1:
        q.append((node, node, cnt + 1))
        dp[node][node] = cnt+1

    # 삭제
    if 0 <= node-1 <= 2*S and dp[node-1][clipboard] == -1:
        q.append(((node - 1), clipboard, cnt + 1))
        dp[node-1][clipboard] = cnt+1

    if clipboard > 0:
        # 붙여넣기
        if 0 <= node+clipboard <= 2*S and dp[node+clipboard][clipboard] == -1:
            q.append((node+clipboard, clipboard, cnt+1))
            dp[node+clipboard][clipboard] = cnt+1

answer = 987654321
for x in dp[S]:
    if not x == -1 and x < answer:
        answer = x

print(answer)

