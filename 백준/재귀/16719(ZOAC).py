import sys
sys.setrecursionlimit(10**6)
s = sys.stdin.readline().strip()
tmp = [''] * len(s)


def divide_conquer(left, right):
    global tmp
    if left == right:
        tmp[left] = s[left]
        print(''.join(tmp))
        return

    min_alpha = min(s[left:right+1])
    min_index = -1
    for i in range(left, right + 1):
        if s[i] == min_alpha:
            min_index = i
            break

    tmp[min_index] = min_alpha
    print(''.join(tmp))

    if not min_index == right:
        divide_conquer(min_index+1, right)
    if not min_index == left:
        divide_conquer(left, min_index-1)
    if len(s) == 1:
        divide_conquer(min_index, min_index)

    return


divide_conquer(0, len(s)-1)

