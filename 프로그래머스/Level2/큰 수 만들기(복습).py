def solution(number, k):
    answer = ''
    number = list(map(int, list(number)))
    stack = [number[0]]
    count = 0
    
    for n in number[1:]:
        if stack and n > stack[-1]:
            while count < k and stack and stack[-1] < n:
                stack.pop(); count += 1
            stack.append(n)
        else: stack.append(n)
    
    answer = "".join(list(map(str,stack)))
    
    if count < k: answer = answer[:-(k-count)]
    
    return answer
