import sys
N, M = map(int, sys.stdin.readline().split())
knownList = list(map(int, sys.stdin.readline().split()))
parent = [x for x in range(N+1)]


def findParent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = findParent(parent[x])
        return parent[x]


def union(a, b):
    pa = findParent(a)
    pb = findParent(b)
    if pa < pb:
        parent[pb] = pa
    else:
        parent[pa] = pb


parties = []
for _ in range(M):
    inputList = list(map(int, sys.stdin.readline().split()))
    parties.append(inputList)

# 진실을 아는 사람이 없다면, 모든 파티에서 거짓말.
if knownList[0] == 0:
    print(M)
    sys.exit(0)

# 먼저 진실을 아는 사람들을 하나의 집합에 묶는다.
tempRoot = knownList[1]
for x in knownList[1:]:
    union(tempRoot, x)

# # 진실을 아는 사람이 있는 파티에 참여한 사람은 모두 같은 집합에 합친다.
# for party in parties:
#     isThereKnownPerson = False
#     knownRoot = findParent(knownList[1])
#
#     for person in party[1:]:
#         if findParent(person) == knownRoot:
#             isThereKnownPerson = True
#             break
#
#     if isThereKnownPerson:
#         for p in party[1:]:
#             union(p, knownRoot)

for party in parties:
    tempRoot = party[1]
    for person in party[1:]:
        union(tempRoot, person)


knownSetRoot = findParent(knownList[1])
answer = 0
# 다시 파티를 훑으면서, known 집합에 없는 사람들만 참여하는 파티에선 거짓말을 한다.
for party in parties:
    can_she_talk_lie = True
    for person in party[1:]:
        if findParent(person) == knownSetRoot:
            can_she_talk_lie = False
            break
    if can_she_talk_lie:
        answer += 1

print(answer)

