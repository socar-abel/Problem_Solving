# 딕셔너리를 이용한 풀이
from collections import deque
from collections import defaultdict
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
N, M, K = map(int, sys.stdin.readline().split())
graph = []
god_str = []
dp = [[defaultdict(int) for _ in range(M)] for _ in range(N)]

for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))

for _ in range(K):
    god_str.append(sys.stdin.readline().strip())

for i in range(N):
    for j in range(M):
        q = deque()
        q.append((i, j, graph[i][j]))
        dp[i][j][graph[i][j]] += 1

        while q:
            x, y, s = q.popleft()
            if len(s) == 5:
                continue

            for d in direction:
                nx = x + d[0]
                ny = y + d[1]

                if nx == N:
                    nx = 0
                if ny == M:
                    ny = 0
                if nx == -1:
                    nx = N-1
                if ny == -1:
                    ny = M-1

                q.append((nx, ny, s + graph[nx][ny]))
                dp[i][j][s + graph[nx][ny]] += 1

for s in god_str:
    ans = 0
    for i in range(N):
        for j in range(M):
            if s in dp[i][j]:
                ans += dp[i][j][s]
    print(ans)



# 트라이를 이용한 풀이
from collections import defaultdict
from collections import deque
import sys
direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
N, M, K = map(int, sys.stdin.readline().split())
graph = []
gods_str = []

for _ in range(N):
    graph.append(list(sys.stdin.readline().strip()))

for _ in range(K):
    gods_str.append(sys.stdin.readline().strip())


class Node:
    def __init__(self, value, flag=None):
        self.children = defaultdict(Node)
        self.value = value
        self.flag = flag
        self.cnt = 0


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]

        if current_node.cnt == 0:
            current_node.flag = string
            current_node.cnt += 1
        else:
            current_node.cnt += 1

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return 0

        if current_node.flag:
            return current_node.cnt
        else:
            return 0


trie = Trie()

for i in range(N):
    for j in range(M):
        q = deque()
        q.append((i, j, graph[i][j]))
        trie.insert(graph[i][j])

        while q:
            x, y, s = q.popleft()
            if len(s) == 5:
                continue

            for d in direction:
                nx = x + d[0]
                ny = y + d[1]

                nx %= N
                ny %= M

                q.append((nx, ny, s + graph[nx][ny]))
                trie.insert(s + graph[nx][ny])

for string in gods_str:
    print(trie.search(string))

