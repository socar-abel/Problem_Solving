import sys
sys.setrecursionlimit(10**6)
N, R, Q = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N+1)]
visit = [False] * (N+1)
# dp[i] = i 를 루트로 하는 서브트리에 속한 노드의 개수
dp = [-1] * (N+1)

for _ in range(N-1):
    U, V = map(int, sys.stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)


def dfs(node):
    visit[node] = True

    if not dp[node] == -1:
        return dp[node]

    dp[node] = 1
    for child in tree[node]:
        if not visit[child]:
            dp[node] += dfs(child)

    return dp[node]


answer = []
dfs(R)
for _ in range(Q):
    U = int(sys.stdin.readline())
    answer.append(dfs(U))

for a in answer:
    print(a)
