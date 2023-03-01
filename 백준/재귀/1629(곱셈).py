import sys
A, B, C = map(int, sys.stdin.readline().split())

def multiple(x, y):
    if y == 1:
        return x % C
    half = multiple(x, y//2)
    if y % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * x) % C

print(multiple(A, B))
