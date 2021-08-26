# 다익스트라 알고리즘으로 해결
import heapq
def solution(n, edges):
    answer = 0; INF = 99999
    graph = [ [] for _ in range(n+1) ]
    distance = [INF] * (n+1)
    distance[1] = 0
    
    for edge in edges:
        node1, node2 = edge[0], edge[1]
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    # dijkstra
    q = []
    heapq.heappush(q,(0,1))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist : continue
        
        for v in graph[now]:
            cost = dist + 1
            if cost < distance[v] : 
                distance[v] = cost
                heapq.heappush(q,(cost,v))
            
    return distance.count(max(distance[1:]))
