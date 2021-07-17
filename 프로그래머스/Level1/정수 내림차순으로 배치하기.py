def solution(n):
    numList = [x for x in str(n)]
    numList.sort(reverse=True)
    return int("".join(numList))
