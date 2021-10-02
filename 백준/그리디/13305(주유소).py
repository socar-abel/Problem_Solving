import sys
N = int(input())
distance = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

answer = price[0] * distance[0]
minPrice = price[0]

i = 1

while i < len(distance):

    if price[i] < minPrice:
        minPrice = price[i]

    answer += minPrice * distance[i]

    i += 1

print(answer)
