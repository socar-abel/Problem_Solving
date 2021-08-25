N, M = 4, 6
cakes = [19,15,10,17]
cakes.sort()
answer = 0
left = 0
right = cakes[-1]
while True:
    print(left, right)
    if left > right : break
    result = 0 
    mid = (left + right) // 2
    print('mid',mid)
    for cake in cakes:
        if cake > mid : result += cake - mid
    
    if result < M : right = mid - 1
    else : answer = mid; left = mid + 1
    print('answer',answer)
    

print(answer)
