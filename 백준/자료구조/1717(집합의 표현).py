import sys
sys.setrecursionlimit(10**6)
N, M = map(int, sys.stdin.readline().split())
parent = [x for x in range(N+1)]
answer = []


def findParent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = findParent(parent[x])
        return parent[x]


for _ in range(M):
    x, a, b = map(int, sys.stdin.readline().split())
    if x == 0:
        pa = findParent(a)
        pb = findParent(b)
        parent[max(pa, pb)] = min(pa, pb)

    elif x == 1:
        if findParent(a) == findParent(b):
            answer.append("YES")
        else:
            answer.append("NO")

for a in answer:
    print(a)
