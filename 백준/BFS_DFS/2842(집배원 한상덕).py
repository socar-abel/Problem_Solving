from collections import deque
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
N = int(sys.stdin.readline())
graph = []
height = []
height_arr = set()
house_arr = set()
num_of_house = 0
P = [0, 0]

for _ in range(N):
    graph.append(list(sys.stdin.readline()))

for _ in range(N):
    height.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for j in range(N):
        height_arr.add(height[i][j])

        if graph[i][j] == 'P':
            P = [i, j]
            house_arr.add(height[i][j])
        elif graph[i][j] == 'K':
            house_arr.add(height[i][j])
            num_of_house += 1

height_arr = sorted(list(height_arr))
house_arr = sorted(list(house_arr))


# 이 고도 차이로 마을 배달을 완료할 수 있는지.
def check(l, r):
    # 모든 집들을 다 방문하는지 수 체크
    k = 0
    visit = [[False] * N for _ in range(N)]
    q = deque()
    q.append((P[0], P[1]))
    visit[P[0]][P[1]] = True

    # 우체국이 범위안에 들어갈 수 없다면
    if (l > height[P[0]][P[1]]) or (r < height[P[0]][P[1]]):
        return False

    while q:
        x, y = q.popleft()
        if graph[x][y] == 'K':
            k += 1

        for d in direction:
            nx = x + d[0]
            ny = y + d[1]

            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if l <= height[nx][ny] <= r:
                    q.append((nx, ny))
                    visit[nx][ny] = True

    return True if k == num_of_house else False


answer = 987654321
max_height = max(height_arr)
max_house = max(house_arr)
min_house = min(house_arr)


for i in range(len(height_arr)):
    temp_min = height_arr[i]
    if temp_min > min_house:
        break
    # 구간의 최댓값을 이분 탐색
    left = max_house
    right = max_height
    answer_of_max = 987654321

    while left <= right:
        mid = (left + right) // 2
        result = check(temp_min, mid)
        if result:
            answer_of_max = mid
            right = mid - 1
        else:
            left = mid + 1

    answer = min(answer, answer_of_max - temp_min)

print(answer)
