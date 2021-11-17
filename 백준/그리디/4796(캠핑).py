import sys

i = 1
while True:
    L, P, V = map(int, sys.stdin.readline().split())

    if L == P == 0 == V:
        break

    if (V%P) < L:
        answer = "Case "+str(i)+": "+str( (V//P)*L + (V%P) )
        print(answer)
    else:
        answer = "Case "+str(i)+": "+str( (V//P)*L + L )
        print(answer)

    i += 1
