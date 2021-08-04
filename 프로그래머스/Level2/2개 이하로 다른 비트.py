# 이거 다른 답안 보니까 미친놈있던데

def binary(x):
    binary = format(x,'b')
    binary = '0'*(50-len(binary)) + binary
    return binary

def f(x):
    bX = binary(x)
    if bX[-2:] == '00' : bX = bX[:-2] + '01'
    elif bX[-2:] == '01' : bX = bX[:-2] + '10'
    elif bX[-2:] == '10' : bX = bX[:-2] + '11'
    elif bX[-2:] == '11':
        i = -1
        while True:
            if bX[i] == '0': break
            i -= 1
        bX = bX[:i] + '10' + bX[i+2:]
    return int(bX,2)

def solution(numbers):
    answer = []
    for x in numbers:
        answer.append(f(x))
    return answer


