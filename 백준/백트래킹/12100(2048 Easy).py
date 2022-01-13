import sys
from collections import defaultdict
from collections import deque
import copy
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
graph = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))


def move(board, idx):
    movedBlocks = []

    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                x, y = i, j
                while True:
                    nx = x + direction[idx][0]
                    ny = y + direction[idx][1]
                    if 0 <= nx < N and 0 <= ny < N:
                        x, y = nx, ny
                    else:
                        break
                # 도착 좌표, 원래좌표, 숫자 값, 움직인 거리
                movedBlocks.append(((x, y), (i, j), board[i][j], max(abs(i-x), abs(j-y))))

    arrivedLocation = defaultdict(list)
    for block in movedBlocks:
        arrivedLocation[(block[0][0], block[0][1])].append((block[1][0], block[1][1], block[2], block[3]))

    # key = 도착좌표
    for key in arrivedLocation:
        # (원래x, 원래y, 숫자값, 움직인 거리)
        arrivedBlockList = arrivedLocation[key]

        if len(arrivedBlockList) == 1:
            block = arrivedBlockList[0]
            board[key[0]][key[1]] = block[2]
            if (key[0], key[1]) != (block[0], block[1]):
                board[block[0]][block[1]] = 0
        else:
            # distance 로 정렬
            arrivedBlockList.sort(key=lambda x: x[3])
            # 스택에 도착한 블록들을 쌓음
            # 스택에는 (값, 변화여부) 를 넣음
            stack = deque()
            for block in arrivedBlockList:
                if not stack:
                    stack.append((block[2], False))
                else:
                    # 스택 탑의 숫자와 현재 넣을 블럭의 숫자가 같다면
                    if (not stack[-1][1]) and stack[-1][0] == block[2]:
                        stack.pop()
                        stack.append((block[2]*2, True))
                    else:
                        stack.append((block[2], False))

                # 스택처리가 끝났으면 그 라인 value 재배치
                i, j = key[0], key[1]

                for newValue in stack:
                    board[i][j] = newValue[0]
                    i -= direction[idx][0]
                    j -= direction[idx][1]

                while 0 <= i < N and 0 <= j < N:
                    board[i][j] = 0
                    i -= direction[idx][0]
                    j -= direction[idx][1]
    return board


answer = 0


def dfs(board, cnt):
    global answer
    if cnt == 5:
        answer = max(answer, max(sum(board, [])))
        return

    for i in range(4):
        copyBoard = copy.deepcopy(board)
        newBoard = move(copyBoard, i)
        dfs(newBoard, cnt + 1)
    return


dfs(graph, 0)
print(answer)

