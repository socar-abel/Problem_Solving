import sys
N = list(sys.stdin.readline().strip())
N.sort(reverse=True)

print(''.join(N))
