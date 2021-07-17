import math
def solution(n):
    array = [True for x in range(n+1)]
    
    for i in range(2,int(math.sqrt(n))+1):
        if array[i] == True:
            j = 2
            while i * j <= n:
                array[i*j] = False
                j += 1
    
    answer = array.count(True)-2
    return answer
