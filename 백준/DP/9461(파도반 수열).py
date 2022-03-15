import sys
T = int(sys.stdin.readline())
num = []
for _ in range(T):
    num.append(int(sys.stdin.readline()))

arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(11, 101):
    now = arr[i-1] + arr[i-5]
    arr.append(now)

for n in num:
    print(arr[n])
