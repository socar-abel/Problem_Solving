import heapq
def solution(n, edge):
    answer = 0; INF = 987654321
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    for e in edge:
        graph[e[0]].append((e[1],1))
        graph[e[1]].append((e[0],1))

    def dijkstra(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist: continue
            
            for i in graph[now]:
                cost = dist + i[1]
                
                if cost < distance[i[0]]: 
                    distance[i[0]] = cost
                    heapq.heappush(q,(cost,i[0]))

    dijkstra(1)               

    return distance.count(max(distance[1:]))
