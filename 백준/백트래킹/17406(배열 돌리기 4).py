import sys
from itertools import permutations
from collections import deque
import copy

answer = sys.maxsize
N, M, K = map(int, sys.stdin.readline().split())
graph = []
cmds = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for _ in range(K):
    cmds.append(list(map(int, sys.stdin.readline().split())))

order_combinations = list(permutations(range(K)))


def one_line_rotate(x1, y1, x2, y2):
    order = []
    items = deque()
    for i in range(y1, y2):
        order.append((x1, i))
        items.append(graph[x1][i])
    for i in range(x1, x2):
        order.append((i, y2))
        items.append(graph[i][y2])
    for i in reversed(range(y1+1, y2+1)):
        order.append((x2, i))
        items.append(graph[x2][i])
    for i in reversed(range(x1+1, x2+1)):
        order.append((i, y1))
        items.append(graph[i][y1])
    items.rotate(1)
    for i in range(len(order)):
        x, y = order[i]
        graph[x][y] = items[i]


def rotate(r, c, s):
    for d in range(1, s + 1):
        one_line_rotate(r-d-1, c-d-1, r+d-1, c+d-1)


origin_graph = copy.deepcopy(graph)

for combi in order_combinations:
    graph = copy.deepcopy(origin_graph)
    temp_answer = sys.maxsize
    for idx in combi:
        cmd = cmds[idx]
        rotate(cmd[0], cmd[1], cmd[2])
    for row in range(len(graph)):
        temp_answer = min(temp_answer, sum(graph[row]))
    answer = min(answer, temp_answer)


print(answer)
