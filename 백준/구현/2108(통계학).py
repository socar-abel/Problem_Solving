import sys
from collections import defaultdict
N = int(sys.stdin.readline())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

one = sum(numbers)/N
if (one*10)%10 >= 5:
    print( sum(numbers)//N + 1 )
else:
    print( sum(numbers)//N )

print(sorted(numbers)[N//2])

counting = defaultdict(int)
for x in numbers:
    counting[x] += 1

max_value = 0
max_keys = []

for key in counting:
    max_value = max(max_value, counting[key])

for key in counting:
    if counting[key] == max_value:
        max_keys.append(key)

if len(max_keys) == 1:
    print(max_keys[0])
else:
    print(sorted(max_keys)[1])


print(max(numbers)-min(numbers))
