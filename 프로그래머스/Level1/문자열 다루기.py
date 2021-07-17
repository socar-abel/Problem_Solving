def solution(s):
    length = True if len(s) == 4 or len(s) == 6 else False
    digit = True
    for i in s :
        if not i.isdigit():
            digit = False
            
    answer = length and digit
    return answer
