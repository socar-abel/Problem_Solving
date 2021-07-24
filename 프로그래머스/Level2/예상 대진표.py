def next(x):
    return x//2 if x % 2 == 0 else x//2 + 1
    
def solution(n,a,b):
    count = 1
    
    while not ( abs(a-b) == 1 and max(a,b) % 2 == 0 ):
        a = next(a)
        b = next(b)
        count += 1

    return count
