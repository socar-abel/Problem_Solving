import sys
import copy
N, M = map(int, sys.stdin.readline().split())
magic_direction = [(99, 99), (-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우
destroy_bubble_num = [0, 0, 0, 0] # 폭발한 구슬의 개수
graph = []
magic = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    magic.append(list(map(int, sys.stdin.readline().split())))

# 달팽이 돌기
position_to_num = [[-1] * N for _ in range(N)]
num_to_position = dict()

i, j, n, d = 0, 0, (N*N) - 1, 0
rotate_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상
position_to_num[0][0] = (N*N) - 1
num_to_position[(N*N) - 1] = (0, 0)

while n > 0:
    ni = i + rotate_direction[d][0]
    nj = j + rotate_direction[d][1]

    # 경계를 만나기 전까지는 그 방향대로 채워감
    if 0 <= ni < N and 0 <= nj < N and position_to_num[ni][nj] == -1:
        n -= 1
        position_to_num[ni][nj] = n
        num_to_position[n] = (ni, nj)
        i, j = ni, nj
    # 경계를 만났거나 이미 간 곳 이면 방향을 틀음
    else:
        d = (d + 1) % 4
        i = i + rotate_direction[d][0]
        j = j + rotate_direction[d][1]
        n -= 1
        position_to_num[i][j] = n
        num_to_position[n] = (i, j)

bubble_arr = [-1] * (N*N)
bubble_arr[0] = "Shark"

# 구슬 배열에 달팽이 순서대로 구슬 삽입
for n in range(1, N*N):
    x, y = num_to_position[n]
    bubble_arr[n] = graph[x][y]


# 4개 이상의 연속된 구슬을 찾으면 파괴시키는 함수
def find_4_bubbles(arr):
    there_is_4bubbles = False
    segment = [0, 0]
    now = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == now:
            segment[1] = i
        else:
            # 구간의 길이가 4가 넘었으면 모두 파괴
            if segment[1] - segment[0] + 1 >= 4 and not now == 0:
                destroy_bubble_num[now] += segment[1] - segment[0] + 1
                there_is_4bubbles = True
                for s in range(segment[0], segment[1] + 1):
                    arr[s] = -2
            segment[0] = i
            now = arr[i]

    new_arr = []
    for a in arr:
        if a != -2:
            new_arr.append(a)

    l = len(new_arr)
    while True:
        if l == len(arr):
            break
        new_arr.append(-1)
        l += 1

    return [there_is_4bubbles, new_arr]


# 1. 블리자드 마법 구슬 파괴 / 2. 연속 구슬 폭발 / 3. 구슬 변화
for m in magic:
    d, s = m[0], m[1]
    x, y = (N-1)//2, (N-1)//2

    # -- 1. 블리자드 마법 수행
    # 범위 내의 구슬 파괴하기
    for i in range(1, s+1):
        # 구슬을 파괴할 좌표
        nx = x + magic_direction[d][0] * i
        ny = y + magic_direction[d][1] * i
        num = position_to_num[nx][ny]
        # 구슬 배열에서 구슬 삭제
        bubble_arr[num] = -2

    # 구슬 재배치
    new_bubble_arr = []
    for a in bubble_arr:
        if a != -2:
            new_bubble_arr.append(a)

    l = len(new_bubble_arr)
    while True:
        if l == len(bubble_arr):
            break
        new_bubble_arr.append(0)
        l += 1

    bubble_arr = new_bubble_arr

    # -- 2. 연속 구슬 폭발
    is_there_4_bubbles, destroyed_bubble_arr = find_4_bubbles(bubble_arr)
    if is_there_4_bubbles:
        go = True
        while go:
            bubble_arr = destroyed_bubble_arr
            result, destroyed_bubble_arr = find_4_bubbles(bubble_arr)
            if not result:
                go = False

    # -- 3. 구슬 변화
    groups = []
    # A = 그룹에 들어있는 구슬의 개수, B = 그룹을 이루고 있는 구슬의 번호
    # 만약 여기서 bubble_arr[1] 이 0 이라면 ?..
    temp_group = [1, bubble_arr[1]]
    for i in range(2, N * N):
        if temp_group[1] == bubble_arr[i]:
            temp_group[0] += 1
        else:
            if temp_group[1] > 0:
                groups.append(temp_group)
            temp_group = [1, bubble_arr[i]]

    final_bubble_arr = ['Shark']
    size_of_final_bubble_arr = 1

    stop_append = False
    for group in groups:
        for i in range(2):
            final_bubble_arr.append(group[i])
            size_of_final_bubble_arr += 1
            if size_of_final_bubble_arr == N * N:
                stop_append = True
                break
        if stop_append:
            break

    while size_of_final_bubble_arr < N * N:
        final_bubble_arr.append(0)
        size_of_final_bubble_arr += 1

    bubble_arr = final_bubble_arr

print(1*destroy_bubble_num[1] + 2*destroy_bubble_num[2] + 3*destroy_bubble_num[3])


