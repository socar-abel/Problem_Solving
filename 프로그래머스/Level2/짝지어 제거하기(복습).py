def solution(string):
    stack = [string[0]]
    
    for s in string[1:]:
        if not stack: stack.append(s)
        else:
            if stack[-1] == s: stack.pop()
            else: stack.append(s)

    return 1 if len(stack) == 0 else 0
