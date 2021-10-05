from itertools import combinations
import sys
N = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
opposite = [(0,5), (5,0), (1,4), (4,1), (2,3), (3,2)]

pair3 = list(combinations(range(6), 3))
pair2 = list(combinations(range(6), 2))

threeSum = 987654321
twoSum = 987654321
oneSum = min(dice)

for a, b, c in pair3:
    if (a, b) in opposite or (b, c) in opposite or (c, a) in opposite:
        continue
    if dice[a]+dice[b]+dice[c] < threeSum:
        threeSum = dice[a]+dice[b]+dice[c]

for a, b in pair2:
    if (a, b) in opposite:
        continue
    if dice[a]+dice[b] < twoSum:
        twoSum = dice[a]+dice[b]

if N == 1:
    possible = []
    for i in range(6):
        possible.append(sum(dice)-dice[i])
    print(min(possible))
else:
    threeFace = 4
    twoFace = 4*(N-1) + 4*(N-2)
    oneFace = 4*(N-1)*(N-2) + (N-2)*(N-2)

    face = [threeFace, twoFace, oneFace]
    face.sort()

    print(threeFace*threeSum + twoFace*twoSum \
          + oneFace*oneSum)
