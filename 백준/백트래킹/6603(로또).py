import sys
from itertools import combinations
testCase = []

while True:
    inputList = list(map(int, sys.stdin.readline().split()))
    if len(inputList) == 1:
        break
    testCase.append(inputList)

for t in testCase:
    combs = list(combinations(t[1:], 6))
    for comb in combs:
        for x in comb:
            print(x, end=' ')
        print()
    print()

