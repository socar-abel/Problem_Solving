import sys
T = int(sys.stdin.readline())


def program():
    N = int(sys.stdin.readline())
    phoneNumber = []
    for _ in range(N):
        number = sys.stdin.readline().strip()
        phoneNumber.append(number)

    answer = 'YES'
    phoneNumber.sort()
    for i in range(1, N):
        if phoneNumber[i][:len(phoneNumber[i-1])] == phoneNumber[i-1]:
            answer = 'NO'
            break

    print(answer)


for _ in range(T):
    program()
