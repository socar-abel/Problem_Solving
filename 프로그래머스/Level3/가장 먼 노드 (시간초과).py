# N이 2000 이라서 다익스트라 알고리즘을 사용했어야 한다. 플로이드 워셜로 풀어서 시간초과 남.

def solution(n, edges):
    answer = 0; INF = 99999
    graph = [ [] for _ in range(n+1) ]
    
    for edge in edges:
        node1, node2 = edge[0], edge[1]
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    distance = [ [INF] * (n+1) for _ in range(n+1) ]
    
    for i in range(n+1): distance[i][i] = 0
    
    for i in range(n+1):
        nodes = graph[i]
        for node in nodes:
            distance[i][node] = 1
        
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                distance[a][b] = min(distance[a][b], distance[a][k]+distance[k][b])

    return distance[1][1::].count(max(distance[1][1::]))
