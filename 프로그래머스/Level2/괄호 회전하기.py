# 나 너무 깔끔하게 짠듯;

def match(a,b):
    pair = [('(',')'), ('{','}'),('[',']')]
    return True if (a,b) in pair else False

def isCorrect(string):
    stack = [string[0]]
    for s in string[1:]:
        if stack and match(stack[-1],s) : stack.pop()
        else : stack.append(s)
    
    return True if not stack else False

def solution(string):
    answer = 0
    
    l = len(string)
    string *= 2
    
    for i in range(l):
        if isCorrect(string[i:l+i]) : answer += 1
    
    return answer
