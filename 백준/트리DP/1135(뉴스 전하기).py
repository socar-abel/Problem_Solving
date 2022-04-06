import sys
N = int(sys.stdin.readline())
relation = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(N+1)]
dp = [-1] * N
visit = [False] * N

for i in range(1, len(relation)):
    tree[relation[i]].append(i)


def dfs(node):
    #print("dfs",node)
    visit[node] = True
    dp[node] = 0
    children = []
    for x in tree[node]:
        if not visit[x]:
            dfs(x)
            children.append(dp[x])

    # dp 값으로 오름차순 정렬
    children.sort(reverse=True)
    #print('dfs',node,'children :',children)
    for c in range(len(children)):
        dp[node] = max(dp[node], c + 1 + children[c])

    #print("dfs",node,'return',dp[node])
    return dp[node]


dfs(0)
print(dp[0])
