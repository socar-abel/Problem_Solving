def reverse(s):
    s = s.replace('(','a').replace(')','b')
    s = s.replace('a',')').replace('b','(')
    return s

def isBalanced(p):
    if not p : return True
    
    stack = [p[0]]
    
    i = 1
    while True:
        if i >= len(p) : break
            
        if stack and stack[-1] == '(' and p[i] == ')':
            stack.pop()
            i += 1
        else:
            stack.append(p[i])
            i += 1
        #print(stack)
    
    return True if len(stack) == 0 else False
        
        
def func(string):
    if string == "" : return ""  #1
    if isBalanced(string) : return string   #0
    
    else:
        u = ""
        v = ""
        
        for i in range(len(string)):
            u += string[i]
            if u.count("(") == u.count(")") : break
        
        v = string[i+1:]
        
        #print(u)
        #print(v)       #2
        
        if isBalanced(u) : return u + func(v)   #3
        else : #4
            temp = "("  #4-1
            temp += func(v) #4-2
            temp += ")" #4-3
            
            u = reverse(u[1:-1])

            temp += u   #4-4
            
            return temp
            
def solution(p):

    # print(isBalanced(p))
    answer = func(p)
    
    return answer
