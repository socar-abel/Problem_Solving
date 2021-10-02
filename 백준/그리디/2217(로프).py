import sys
N = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(N)]
rope.sort()

possible = []
for i in range(N):
    possible.append(rope[i]*(N-i))

print(max(possible))
