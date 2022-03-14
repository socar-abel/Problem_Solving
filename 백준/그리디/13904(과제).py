import sys
N = int(sys.stdin.readline())
homeworks = []
visit = [False] * 1001

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    homeworks.append((d, w))

homeworks.sort(key=lambda x: x[1], reverse=True)
answer = 0
for day, worth in homeworks:
    i = day
    # 과제를 할 날짜 탐색
    while i > 0 and visit[i]:
        i -= 1
    # 과제를 할 날짜가 없으면 패스
    if i == 0:
        continue
    else:
        visit[i] = True
        answer += worth

print(answer)
