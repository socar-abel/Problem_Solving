import sys
from collections import defaultdict
N, K = map(int, sys.stdin.readline().split())
answer = 0
nameLen = []

for _ in range(N):
    nameLen.append(len(sys.stdin.readline().strip()))

window = defaultdict(int)
# window 초기 세팅
for i in range(K+1):
    if window[nameLen[i]] > 0:
        answer += window[nameLen[i]]
    window[nameLen[i]] += 1

#print(window)

for i in range(K+1, N):
    window[nameLen[i-K-1]] -= 1

    if window[nameLen[i]] > 0:
        answer += window[nameLen[i]]
    window[nameLen[i]] += 1

    #print(window)

print(answer)
