from itertools import permutations
import math

def is_Prime(x):
    if x == 0 or x == 1 : return False
    
    for i in range(2,int(math.sqrt(x))+1):
        if x % i == 0 : return False
    return True

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    permus = []
    
    for x in range(1,len(numbers)+1):   
        temp = list(permutations(numbers,x))    # O(N!)
        permus.append(temp)
    
    #print(permus)
    candidates = set()
    for permu in permus:    
        for p in permu:         # O(N!)
            num = "".join(p)
            if num[0] == '0' and len(num) >= 2: num = num[1:]
            candidates.add(int(num)) 
        
    #print(candidates)
    
    for candy in candidates:
        if is_Prime(candy) : answer += 1
    
    return answer




