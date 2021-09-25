N = int(input())
x = 0

while N > 0:
    if N % 5 == 0:
        x += N // 5
        N = 0
        break
    else:
        N -= 3
        x += 1

if not N == 0:
    print(-1)
else: print(x)
