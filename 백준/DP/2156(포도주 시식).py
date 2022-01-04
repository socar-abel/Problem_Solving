import sys
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

if N == 1 or N == 2:
    print(sum(arr))
else:
    # dp[i][0] = i 가 있고 최대
    # dp[i][1] = i 가 없고 최대
    dp = [[0] * 2 for _ in range(N)]
    dp[0] = [0, arr[0]]
    dp[1] = [arr[0], arr[0] + arr[1]]
    dp[2] = [arr[0]+arr[1], max(arr[0], arr[1]) + arr[2]]

    for i in range(3, N):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])
        dp[i][1] = max(dp[i-2][0] + arr[i-1],
                       dp[i-1][0]) + arr[i]

    print(max(sum(dp, [])))
