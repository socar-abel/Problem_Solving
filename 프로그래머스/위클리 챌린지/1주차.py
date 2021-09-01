def solution(price, money, count):
    first = price; last = price*count;
    total = count * (first+last) // 2
    return total - money if total > money else 0
