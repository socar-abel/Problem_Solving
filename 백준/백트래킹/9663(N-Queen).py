import sys
N = int(sys.stdin.readline())
answer = 0
direction = [(1, 0), (0, 1), (1, 1), (1, -1)]


def dfs(x, trace):  # x는 현재 행
    global answer
    if len(trace) == N:
        answer += 1
        return

    for y in range(N):
        check = True
        for row, col in trace:
            # 같은 열 제외
            if y == col:
                check = False
                break
            # 대각선 제외
            if abs(x-row) == abs(y-col):
                check = False
                break

        if check:
            trace.append((x, y))
            dfs(x+1, trace)
            trace.pop()


dfs(0, [])
print(answer)
