import sys
T = int(sys.stdin.readline())


def prevCoin(coin, x):
    result = []
    for c in coin:
        if x > c:
            result.append(c)
    return result


def program():
    N = int(sys.stdin.readline())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline())
    dp = [0]*(M+1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, M+1):
            dp[x] += dp[x-coin]
    print(dp[-1])


for _ in range(T):
    program()

