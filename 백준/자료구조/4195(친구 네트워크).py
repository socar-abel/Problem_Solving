import sys
T = int(sys.stdin.readline())


# 경로 압축
def getRoot(x, parent):
    if parent[x] == x:
        return x
    else:
        parent[x] = getRoot(parent[x], parent)
    return parent[x]


def program():
    F = int(sys.stdin.readline())
    parentTable = dict()
    sizeOfSet = dict()

    for _ in range(F):
        A, B = sys.stdin.readline().split()

        # 처음 등장한 노드는 루트를 자신으로 갱신
        if not A in parentTable:
            parentTable[A] = A
        if not B in parentTable:
            parentTable[B] = B

        # 두 노드의 루트를 구함
        rootA = getRoot(A, parentTable)
        rootB = getRoot(B, parentTable)

        # 루트가 같으면 패스
        if rootA == rootB:
            print(sizeOfSet[rootA])
            continue

        # 루트가 더 작은 쪽으로 합침
        minRoot = min(rootA, rootB)
        maxRoot = max(rootA, rootB)
        parentTable[maxRoot] = minRoot

        # 둘 중 작은 루트가 처음으로 등장한 경우, 집합을 새로 만들어줌.
        if not minRoot in sizeOfSet:
            sizeOfSet[minRoot] = 1

        # 둘 중 큰 루트가 이미 집합을 가지고 있던 경우는 합집합.
        if maxRoot in sizeOfSet:
            sizeOfSet[minRoot] += sizeOfSet[maxRoot]
        else:
            sizeOfSet[minRoot] += 1

        print(sizeOfSet[minRoot])


while T:
    program()
    T -= 1
