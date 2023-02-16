import sys
sys.setrecursionlimit(10 ** 6)

def solution(info, edges):
    global answer
    answer = 0
    graph = [[] for _ in range(len(info))]
    for x, y in edges:
        graph[x].append(y)

    def dfs(idx, sheep, wolves, next, visit):
        global answer
        if info[idx] == 0:
            sheep += 1
            answer = max(answer, sheep)
        else:
            wolves += 1

        new_next = [x for x in graph[idx]]

        for x in next + new_next:
            if visit[x]: continue
            if info[x] == 0:
                visit[x] = True
                dfs(x, sheep, wolves, next + new_next, visit)
                visit[x] = False
            else:
                if sheep > wolves + 1:
                    visit[x] = True
                    dfs(x, sheep, wolves, next + new_next, visit)
                    visit[x] = False

    _visit = [False]*len(info)
    _visit[0] = True
    dfs(0, 0, 0, [], _visit)

    return answer

