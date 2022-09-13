import sys
N, K = map(int, sys.stdin.readline().split())

i = N
while True:
    min_count = bin(i).count("1")
    if min_count <= K:
        print(i - N)
        break
    else:
        i += 1
