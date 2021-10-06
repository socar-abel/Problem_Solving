import sys
N, K, B = map(int, sys.stdin.readline().split())
signal = [1] * (N+1)
for _ in range(B):
    signal[int(sys.stdin.readline())] = 0

window = sum(signal[1:K+1])
minBreak = K-window
for i in range(2, N-K+2):
    window = window - signal[i-1] + signal[i-1+K]
    minBreak = min(minBreak, K-window)
    if minBreak == 0:
        break

print(minBreak)
