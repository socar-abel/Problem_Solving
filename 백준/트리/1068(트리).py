import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
parent = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
answer = 0
root = 0

for i in range(N):
    pi = parent[i]
    if pi == -1:
        root = i
        continue
    graph[pi].append(i)


def dfs(node):
    global answer
    # 리프
    if not graph[node]:
        answer += 1
        return

    has_child = False

    for x in graph[node]:
        if not x == M:
            has_child = True
            dfs(x)

    if not has_child:
        answer += 1
        return


dfs(root)
# 루트를 삭제해버린 경우
if parent[M] == -1:
    print(0)
else:
    print(answer)
