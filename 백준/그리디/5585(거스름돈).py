cost = int(input())
cost = 1000 - cost
coin = [500,100,50,10,5,1]
answer = 0

for x in coin:
    if cost // x >= 1:
        n = cost // x
        cost = cost - n * x
        answer += n

print(answer)
