N = int(input())
answer = ''

for i in range(N):
    file = input()
    if i == 0: answer = file[:]
    else:
        for x in range(len(file)):
            if answer[x] != file[x]:
                answer = answer[:x] + '?' + answer[x+1:]

print(answer)
