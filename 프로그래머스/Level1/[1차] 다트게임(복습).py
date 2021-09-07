def solution(dartResult):
    answer = 0
    numbers = []
    dartResult = dartResult.replace('10','X')
    for i in range(len(dartResult)):
        now = dartResult[i]
        if now.isdigit(): numbers.append(int(now))
        elif now == 'X': numbers.append(10)
        elif now == 'S':
            numbers[-1] = numbers[-1]
        elif now == 'D':
            numbers[-1] **= 2
        elif now == 'T':
            numbers[-1] **= 3
        elif now == '*':
            if len(numbers) == 1: numbers[0] *= 2
            else:
                numbers[-1] *= 2
                numbers[-2] *= 2
        elif now == '#':
            numbers[-1] *= -1
    
    return sum(numbers)
