import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)]
# dp[x] = [n, q]
# n = x를 루트로 하는 서브트리에서의 최소 어덥터 수
# q = 루트 x가 어덥터인지 여부
dp = [-1] * (N+1)
visit = [False] * (N+1)
in_degree = [0] * (N+1)
root = 1

for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)
    in_degree[v] += 1


# 리턴 값은 현재 노드가 어댑터가 될 것인지
def dfs(node):
    visit[node] = True

    # 만약 현재 노드가 리프라면
    if not tree[node]:
        dp[node] = 0
        return False

    # 현재 노드가 리프가 아니라면
    all_children_is_adapter = True
    dp[node] = 0
    for child in tree[node]:
        if not visit[child]:
            result = dfs(child)
            dp[node] += dp[child]
            if not result:
                all_children_is_adapter = False

    if all_children_is_adapter:
        return False
    else:
        dp[node] += 1
        return True


dfs(root)
print(dp[root])
