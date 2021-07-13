def solution(n):
    answer = 0
    ternary = ''

    while n > 0:
        div = n // 3
        mod = n % 3
        n = div
        ternary += str(mod)

    list = ternary[::-1]

    for i in range(len(list)):
        answer += int(list[i])*(3**i)

    return answer



# 이런것도 있구나 int()함수의 기능
'''
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
'''
