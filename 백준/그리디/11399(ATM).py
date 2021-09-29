import sys
N = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()
result = 0
tempSum = 0
for x in p:
    tempSum += x
    result += tempSum

print(result)
