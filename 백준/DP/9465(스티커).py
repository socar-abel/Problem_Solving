import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    W = []
    for _ in range(2):
        W.append(list(map(int, sys.stdin.readline().split())))

    if N == 1:
        print(max(W[0][0], W[1][0]))
        continue

    if N == 2:
        answer = max(W[0][0] + W[1][1], W[0][1] + W[1][0])
        print(answer)
        continue

    dp = [[0] * len(W[0]) for _ in range(2)]
    dp[0][0] = W[0][0]
    dp[1][0] = W[1][0]
    dp[0][1] = W[1][0] + W[0][1]
    dp[1][1] = W[0][0] + W[1][1]

    for i in range(2, len(W[0])):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + W[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + W[1][i]

    print(max(dp[0][-1], dp[1][-1]))

