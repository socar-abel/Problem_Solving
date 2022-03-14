import heapq
import sys
N, K = map(int, sys.stdin.readline().split())
gems = []
bags = []

for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    gems.append((M, V))

for _ in range(K):
    C = int(sys.stdin.readline())
    bags.append(C)

gems.sort(key=lambda x: x[0])
bags.sort()
q = []
answer = 0
i = 0

for bag_weight in bags:
    # 지금 이 가방보다 무게가 작은 보석들은 힙에 모두 담는다.
    while (i < N) and (gems[i][0] <= bag_weight):
        # 최대 힙을 위해서 음수 값 저장
        heapq.heappush(q, -gems[i][1])
        i += 1

    if q:
        max_value_gem = -heapq.heappop(q)
        answer += max_value_gem

print(answer)
