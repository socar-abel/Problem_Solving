def solution(numbers):
    answer = ''
    numbers.sort(key = lambda x : str(x)*3, reverse = True)
    return str(int("".join(map(str,numbers))))
