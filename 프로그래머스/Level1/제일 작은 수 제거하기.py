def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) >= 1 else [-1]
