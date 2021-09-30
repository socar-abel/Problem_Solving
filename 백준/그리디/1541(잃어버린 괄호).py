expression = input()
numbers = list(map(int, expression.replace('-', '+').split('+')))
opers = []
for x in expression:
    if not x.isdigit():
        opers.append(x)


idx = len(numbers)
for i in range(len(opers)):
    if opers[i] == '-':
        idx = i
        break

result = 0
for i in range(len(numbers)):
    if i <= idx:
        result += numbers[i]
    else: result -= numbers[i]

print(result)
