import copy
answer = 0


# 현재 노드, 자식 제외 갈 수 있는 곳, 양, 늑대
def dfs(tree, info, node, can_go, sheep, wolves):
    global answer
    answer = max(answer, sheep)
    new_can_go = copy.deepcopy(can_go)

    # 자식 노드가 1개인 경우
    if len(tree[node]) == 1:
        child = tree[node][0]
        if info[child] == 0:
            dfs(tree, info, child, new_can_go, sheep + 1, wolves)
        else:
            if sheep > wolves + 1:
                dfs(tree, info, child, new_can_go, sheep, wolves + 1)
                
    # 자식 노드가 2개인 경우
    if len(tree[node]) == 2:
        for i in range(2):
            child = tree[node][i]
            if info[child] == 0:
                dfs(tree, info, child, new_can_go + [tree[node][(i + 1) % 2]], sheep + 1, wolves)
            else:
                if sheep > wolves + 1:
                    dfs(tree, info, child, new_can_go + [tree[node][(i + 1) % 2]], sheep, wolves + 1)

    # 자식이 아닌 노드로도 갈 수 있다.
    for x in can_go:
        if info[x] == 0:
            new_can_go.remove(x)
            dfs(tree, info, x, new_can_go + tree[node], sheep + 1, wolves)
            new_can_go.append(x)
        else:
            if sheep > wolves + 1:
                new_can_go.remove(x)
                dfs(tree, info, x, new_can_go + tree[node], sheep, wolves + 1)
                new_can_go.append(x)


def solution(info, edges):
    global answer
    answer = 0
    graph = [[] for _ in range(len(info))]

    for parent, child in edges:
        graph[parent].append(child)

    dfs(graph, info, 0, [], 1, 0)

    return answer
