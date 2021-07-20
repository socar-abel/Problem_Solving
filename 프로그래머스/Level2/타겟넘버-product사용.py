from itertools import product

def solution(numbers, target):      
    
    candidate = [(x,-x) for x in numbers]
    cartesian = list(map(sum,product(*candidate)))
    
    return cartesian.count(target)
