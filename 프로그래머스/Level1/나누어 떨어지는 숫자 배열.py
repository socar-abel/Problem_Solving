# or 사용법 배워간 문제

def solution(arr, divisor):
    answer = []
    answer = [x for x in arr if x % divisor == 0]
    answer.sort()
    
    return answer or [-1]
