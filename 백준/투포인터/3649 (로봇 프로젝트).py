import sys
while True:
    try:
        x = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        x = x * (10 ** 7)

        lego = []
        for _ in range(n):
            lego.append(int(sys.stdin.readline()))

        lego.sort()

        left = 0
        right = n - 1
        danger = True

        while left < right:
            if lego[left] + lego[right] == x:
                danger = False
                print('yes', lego[left], lego[right])
                break
            elif lego[left] + lego[right] < x:
                left += 1
            elif lego[left] + lego[right] > x:
                right -= 1

        if danger:
            print('danger')
    except:
        break


