N = int(input())

answer = 0
x = 1
while True:
    if N < x:
        break
    else:
        N -= x
        x += 1
        answer += 1
print(answer)

