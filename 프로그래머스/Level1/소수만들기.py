import math
from itertools import combinations

def isPrime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    combs = list(combinations(nums,3))
    
    for comb in combs:
        tempSum = sum(comb)
        if isPrime(tempSum):
            answer += 1
    
    return answer
