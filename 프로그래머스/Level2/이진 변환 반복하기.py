def step1(s):
    removed = s.count('0')
    result = '1' * s.count('1')
    return (removed,result)

def step2(s):
    l = len(s)
    return format(l,'b')

def solution(s):
    answer = [0,0]
    convert, remove = 0, 0
    while True:
        if s == '1' : answer[0] = convert; answer[1] = remove; break
        r, s = step1(s); remove += r
        s = step2(s); convert += 1
    return answer
