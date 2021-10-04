import sys
number = sys.stdin.readline().strip()

change = 0
temp = number[0]
for i in range(1, len(number)):
    if number[i] != temp:
        change += 1
        temp = number[i]

if change % 2 == 0:
    print(change // 2)
else:
    print((change+1)//2)
