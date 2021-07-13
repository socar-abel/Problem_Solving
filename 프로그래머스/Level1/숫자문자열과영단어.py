def isNum(x):
    num = ['0','1','2','3','4','5','6','7','8','9']
    if x in num:
        return True
    else :
        return False
    
def makeNum(str):
    if str == 'zero':
        return 0
    elif str == 'one':
        return 1
    elif str == 'two':
        return 2
    elif str == 'three':
        return 3
    elif str == 'four':
        return 4
    elif str == 'five':
        return 5
    elif str == 'six':
        return 6
    elif str == 'seven':
        return 7
    elif str == 'eight':
        return 8
    elif str == 'nine':
        return 9
    else :
        return -1
    
def solution(string):
    answer = ''
    temp = ''
    
    for s in string:
        if isNum(s):
            answer += str(s)
        else:
            temp += s
            if makeNum(temp) == -1:
                pass
            else :
                answer += str(makeNum(temp))
                temp = ''

    return int(answer)
