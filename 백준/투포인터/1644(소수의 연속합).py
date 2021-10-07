import sys
import math
N = int(sys.stdin.readline())

arr = [True]*(N+1)
arr[0] = arr[1] = False

if N == 1:
    print(0)
    exit(0)
elif N == 2:
    print(1)
    exit(0)

for i in range(2, int(math.sqrt(N))+1):
    x = 2
    while i * x <= N:
        arr[i*x] = False
        x += 1

prime= []

for i in range(len(arr)):
    if arr[i]:
        prime.append(i)

end = 0
interval_sum = 0
answer = 0

for start in range(len(prime)):
    while end < len(prime) and interval_sum < N:
        interval_sum += prime[end]
        end += 1

    if interval_sum == N:
        answer += 1

    interval_sum -= prime[start]

print(answer)

