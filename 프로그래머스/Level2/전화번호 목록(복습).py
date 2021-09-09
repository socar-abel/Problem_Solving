# 늘었다.. 제한사항 phone_book 크기가 10^6 인 것을 보고 O(N logN)의 알고리즘을 짜야한다고 바로 생각이 들었고, sort()가 O(N logN) time임을 떠올렸다.

def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(1,len(phone_book)):
        if phone_book[i-1] == phone_book[i][:len(phone_book[i-1])]: return False
    
    return answer
