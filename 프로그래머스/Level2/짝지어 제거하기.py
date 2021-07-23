def solution(s):
    stack = [s[0]]
    
    for i in range(1,len(s)):
        if stack:
            top = stack[-1]
            now = s[i]
        else:
            top = -1
            now = s[i]
        
        if top == now : stack.pop()
        else : stack.append(now) 
    
    return 1 if len(stack) == 0 else 0
