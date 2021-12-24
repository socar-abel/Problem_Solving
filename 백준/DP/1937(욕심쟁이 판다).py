import sys
sys.setrecursionlimit(10**6)
n = int(sys.stdin.readline())
graph = []
dp = [[-1]*n for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


def dfs(x, y):
    # 이미 처리했을 경우 dp 값 사용
    if dp[x][y] != -1:
        return dp[x][y]
    # 처리하지 않은 경우
    else:
        # 지금 먹은 곳 1.
        dp[x][y] = 1
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < n and graph[x][y] < graph[nx][ny]:
                # for 문을 도는 동안 최댓값이 교체될 수 있기 때문에 max 함수 사용
                # 1 + dfs(nx, ny) 인 이유는 현재 먹은 곳 (1) + 다음 먹으러 갈 곳 (dfs) 이기 때문
                dp[x][y] = max(dp[x][y], 1 + dfs(nx, ny))
        # go = True, False 와 같은 플래그를 사용하지 않아도 된다.
        return dp[x][y]


for i in range(n):
    for j in range(n):
        dfs(i, j)
# sum 을 이용한 2차원 -> 1차원 배열 변경
print(max(sum(dp, [])))
