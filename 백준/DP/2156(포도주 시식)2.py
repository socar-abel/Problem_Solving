import sys
N = int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))

if N == 1 or N == 2:
    print(sum(arr))
else:
    # dp[i] = i 까지 고려했을 때 최대
    dp = [0] * N
    dp[0] = arr[0]
    dp[1] = sum(arr[:2])
    dp[2] = max(dp[1], arr[0] + arr[2], arr[1] + arr[2])

    for i in range(3, N):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    print(max(dp))
