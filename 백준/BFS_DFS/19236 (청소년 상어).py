import copy
import sys
sys.setrecursionlimit(10**6)
direction = [(-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
board = [[] for _ in range(4)]
# 물고기 번호 : 물고기 좌표
fish_dict = dict()
answer = 0

for i in range(4):
    input_list = list(map(int, sys.stdin.readline().split()))
    for j in range(0, 8, 2):
        board[i].append([input_list[j], input_list[j+1]])
        fish_dict[input_list[j]] = [i, j // 2]


# 좌표, 상어 방향, 먹은 물고기 합
def dfs(g, x, y, eat, fish_position):
    global answer
    graph = copy.deepcopy(g)
    fish = copy.deepcopy(fish_position)

    # 이 좌표의 물고기를 먹었으므로 딕셔너리에서 삭제
    del fish[graph[x][y][0]]
    # 먹은 물고기 번호 합
    eat += graph[x][y][0]

    # 먹은 물고기의 방향이 상어의 방향이 된다.
    shark_direction = graph[x][y][1]
    graph[x][y] = ['S', shark_direction]

    # 물고기 대 이동
    for n in range(1, 17):
        # 이 번호의 물고기가 그래프에 남아있다면 이동을 준비한다.
        if n in fish:
            fish_x = fish[n][0]
            fish_y = fish[n][1]
            fish_d = graph[fish_x][fish_y][1]
            # 8 방향 탐색
            for d in range(8):
                fish_nx = fish_x + direction[(fish_d + d) % 8][0]
                fish_ny = fish_y + direction[(fish_d + d) % 8][1]
                # 경계 안이고, 상어가 없는 곳이라면 물고기 스왑
                if 0 <= fish_nx < 4 and 0 <= fish_ny < 4 and (not graph[fish_nx][fish_ny][0] == 'S'):
                    # 방향 전환
                    graph[fish_x][fish_y][1] = (fish_d + d) % 8

                    # 물고기가 있는 곳이라면 next_fish 딕셔너리 갱신
                    if not graph[fish_nx][fish_ny][0] == 0:
                        next_fish_num = graph[fish_nx][fish_ny][0]
                        fish[next_fish_num] = [fish_x, fish_y]

                    # 그래프 변경
                    graph[fish_x][fish_y], graph[fish_nx][fish_ny] = graph[fish_nx][fish_ny], graph[fish_x][fish_y]
                    fish[n] = [fish_nx, fish_ny]
                    break

    # 상어가 물고기를 먹으러 갈 수 있는 칸이 있는지
    shark_can_go_to_eat = False
    for i in range(1, 4):
        nx = x + direction[shark_direction % 8][0] * i
        ny = y + direction[shark_direction % 8][1] * i

        # 갈 수 있는 칸이 있다면 이동
        if 0 <= nx < 4 and 0 <= ny < 4 and (not graph[nx][ny][0] == 0):
            shark_can_go_to_eat = True
            # 상어가 먹고 떠날 자리는 0 으로 변경
            graph[x][y] = [0, 0]
            dfs(graph, nx, ny, eat, fish)

    if not shark_can_go_to_eat:
        answer = max(answer, eat)


dfs(board, 0, 0, 0, fish_dict)
print(answer)

