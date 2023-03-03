import sys
N, r, c = map(int, sys.stdin.readline().split())
answer = 0

def dfs(start_num, x, y, size):
    if size == 1:
        global answer
        answer = start_num
        return

    section_count = (size*size)//4

    if x < size//2 and y < size//2:
        dfs(start_num, x, y, size//2)
    elif x < size//2 and y >= size//2:
        dfs(start_num + section_count, x, y - size//2, size//2)
    elif x >= size//2 and y < size//2:
        dfs(start_num + section_count*2, x - size//2, y, size//2)
    else:
        dfs(start_num + section_count*3, x - size//2, y - size//2, size//2)

dfs(0, r, c, 2**N)
print(answer)
