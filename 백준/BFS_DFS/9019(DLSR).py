from collections import deque
import sys
T = int(sys.stdin.readline())
cmd = []
answers = []


def makeZero(x):
    if not len(x) == 4:
        while not len(x) == 4:
            x = '0' + x
    return x


def D(x):
    x = int(x)
    x *= 2
    if x > 9999:
        x %= 10000
    return makeZero(str(x))


def S(x):
    if x == '0000':
        return "9999"
    else:
        x = int(x)
        x -= 1
        result = makeZero(str(x))
        return result


def L(x):
    y = x[1:] + x[0]
    return y


def R(x):
    y = x[3] + x[:3]
    return y


for _ in range(T):
    cmd.append(list(sys.stdin.readline().split()))

for c in cmd:
    A, B = c[0], c[1]
    visit = [False] * 10000

    A = makeZero(A)
    B = makeZero(B)

    q = deque()
    q.append((A, ''))
    visit[int(A)] = True

    while q:
        now, path = q.popleft()

        if now == B:
            answers.append(path)
            break

        d = D(now)
        s = S(now)
        l = L(now)
        r = R(now)

        if 0 <= int(d) < 10000 and not visit[int(d)]:
            q.append((d, path + 'D'))
            visit[int(d)] = True

        if 0 <= int(s) < 10000 and not visit[int(s)]:
            q.append((s, path + 'S'))
            visit[int(s)] = True

        if 0 <= int(l) < 10000 and not visit[int(l)]:
            q.append((l, path + 'L'))
            visit[int(l)] = True

        if 0 <= int(r) < 10000 and not visit[int(r)]:
            q.append((r, path + 'R'))
            visit[int(r)] = True


for answer in answers:
    print(answer)

