import sys

N, M = map(int, sys.stdin.readline().split())

num = [i for i in range(1, N + 1)]


def dfs(trace):
    if len(trace) == M:
        for t in trace:
            print(t, end=' ')
        print()
        return

    for i in range(1, N + 1):
        if not i in trace:
            trace.append(i)
            dfs(trace)
            trace.pop()


dfs([])
