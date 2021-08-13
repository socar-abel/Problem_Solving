def solution(n):
    binN = format(n,'b')
    one = binN.count('1')
    
    while True:
        n += 1
        tempBin = format(n,'b')
        tempOne = tempBin.count('1')
        if one == tempOne : answer = n; break
    
    return n
