def solution(ss):
    answer = True
    if ss[0] == ')' : return False
    stack = [ss[0]]
    for s in ss[1:]:
        if stack and stack[-1] == '(' and s == ')' : stack.pop()
        else : stack.append(s)
            
    return True if not stack else False
