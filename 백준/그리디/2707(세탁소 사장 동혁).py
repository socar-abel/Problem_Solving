T = int(input())
q = d = n = p = 0

while T > 0:

    C = int(input())

    q = C // 25
    d = (C % 25) // 10
    n = ((C % 25) % 10) // 5
    p = ((C % 25) % 10) % 5

    print(q,d,n,p)

    T -= 1
