selfNum = [True] * 10001

def makeD(n):
    nextN = n
    for s in str(n):
        nextN += int(s)

    if nextN <= 10000:
        selfNum[nextN] = False
        makeD(nextN)


for i in range(1, 10001):
    makeD(i)

for i in range(1, 10001):
    if selfNum[i]: print(i)
