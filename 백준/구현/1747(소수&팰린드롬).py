import sys
import math
N = int(sys.stdin.readline())


def isPrime(x):
    if x == 1:
        return False
    for n in range(2, int(math.sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True


def isPalindrome(num):
    result = True
    for x in range(len(num)):
        if num[x] != num[len(num) - 1 - x]:
            result = False
            break
    return result


i = N
while True:
    if isPrime(i) and isPalindrome(str(i)):
        print(i)
        break
    i += 1

