import math

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    
    else:
        if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2:
            print(0)
        elif abs(r1 - r2) == distance or r1 + r2 == distance:
            print(1)
        else:
            print(2)
