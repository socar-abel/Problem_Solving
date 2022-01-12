from itertools import permutations
import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
perms = list(permutations(arr, N))
answer = 0


def getResult(permList):
    result = 0
    for i in range(N-1):
        result += abs(permList[i] - permList[i+1])
    return result


for perm in perms:
    answer = max(answer, getResult(list(perm)))

print(answer)
