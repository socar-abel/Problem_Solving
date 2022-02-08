import sys
N = int(sys.stdin.readline())
people = []
ranks = []

for _ in range(N):
    weight, height = map(int, sys.stdin.readline().split())
    people.append((weight, height))

for person in people:
    k = 0
    for i in range(N):
        if person[0] < people[i][0] and person[1] < people[i][1]:
            k += 1
    ranks.append(k+1)

for rank in ranks:
    print(rank, end=' ')
