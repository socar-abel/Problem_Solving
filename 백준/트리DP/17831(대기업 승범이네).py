import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
parent = [0] + [0] + list(map(int, sys.stdin.readline().split()))
W = [0] + list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
visit = [False] * (N+1)

for i in range(2, N+1):
    tree[parent[i]].append(i)


def dfs(node):
    visit[node] = True

    for x in tree[node]:
        dfs(x)
        dp[node][0] += max(dp[x][0], dp[x][1])

    dp[node][1] = dp[node][0]
    for x in tree[node]:
        dp[node][1] = max(dp[node][1], dp[node][0] - max(dp[x][0], dp[x][1]) + (W[node] * W[x]) + dp[x][0])


dfs(1)
print(max(dp[1]))


