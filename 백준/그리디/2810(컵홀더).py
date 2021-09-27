import sys

N = int(sys.stdin.readline())

people = str(sys.stdin.readline()).strip()

answer = 1
i = 0

while i < len(people):
    if answer >= len(people):
        break

    if people[i] == 'S':
        answer += 1
        i += 1
    elif people[i] == 'L':
        answer += 1
        i += 2

print(answer)
