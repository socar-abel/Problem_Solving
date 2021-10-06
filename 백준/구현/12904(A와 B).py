import sys
S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

for _ in range(len(T)-len(S)):
    if T[-1] == 'A':
        T = T[:-1]
        #print(T)
    elif T[-1] == 'B':
        T = T[:-1][::-1]
        #print(T)

if S == T:
    print(1)
else:
    print(0)
