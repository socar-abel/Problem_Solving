import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
oper = [0, 0, 0, 0]    # + - * /
oper[0], oper[1], oper[2], oper[3] = map(int, sys.stdin.readline().split())

minV = 10**9
maxV = -10**9


def dfs(x, result, op):
    global minV, maxV

    if x == N-1:
        minV = min(minV, result)
        maxV = max(maxV, result)
        return

    for i in range(4):
        if op[i] >= 1:
            op[i] -= 1
            if i == 0:
                dfs(x+1, result + num[x + 1], op)
            elif i == 1:
                dfs(x+1, result - num[x + 1], op)
            elif i == 2:
                dfs(x+1, result * num[x + 1], op)
            elif i == 3:
                if result < 0:
                    dfs(x+1, -(-result // num[x+1]), op)
                else:
                    dfs(x+1, result // num[x + 1], op)
            op[i] += 1


dfs(0, num[0], oper)

print(maxV)
print(minV)
