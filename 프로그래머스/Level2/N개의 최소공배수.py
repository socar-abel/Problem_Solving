from math import gcd
def lcm(x,y):
    return (x*y)//gcd(x,y)

def solution(arr):
    answer = 0
    before = arr[0]
    i = 1
    while True:
        if i >= len(arr) : break
        answer = lcm(before,arr[i])
        before = answer
        i += 1
    
    return answer
