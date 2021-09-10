'''
여기서 왜 left로 return 할 때는 정답이고 mid로 return 할 때는 오답인지 깊게 이해해야한다.
left <= right인데 left랑 mid가 다르게 끝나는 순간이 있나? 생각햇는데
left = 11, right = 13이고 여기서 possible값이 n보다 크면 right = 11이 된채로 while문이 끝나버린다. while문 안에 들어가야만 mid = (11+11)//2 = 11 이 될 텐데, 그전에 끝나서 12인 상태로 남아있게 되는 것이다..
'''
def solution(n, times):
    left = 0; right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        
        possible = 0
        for time in times:
            possible += mid // time
        
        if possible >= n: right = mid-1
        else: left = mid+1
    
    return left
