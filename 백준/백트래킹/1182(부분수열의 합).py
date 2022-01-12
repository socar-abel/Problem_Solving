from itertools import combinations
import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(1, N+1):
    tempComb = list(combinations(arr, i))
    for comb in tempComb:
        if sum(comb) == S:
            answer += 1

print(answer)
