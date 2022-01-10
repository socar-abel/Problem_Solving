import sys
N, M = map(int, sys.stdin.readline().split())
arr = []


def dfs(num, path, cnt):
    if cnt == M:
        arr.append(path)
        return

    for i in range(num, N+1):
        dfs(i, path+' '+str(i), cnt+1)


for i in range(1, N+1):
    dfs(i, str(i), 1)


for x in arr:
    print(x)
