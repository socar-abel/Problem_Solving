# 테케 26번이 자꾸 초과됨 ; resultEach, resultTogether이거 다 없애고 return에 한꺼번에 때려박으니까 해결됨
# INF = 987654321로 하는게 가장 좋은듯.
# result가 최소가 되도록 한다. result는 A.B 합승하거나 따로 갈때를 모두 고려한다.
# result = AB 같이 가는 길 + A 따로 가는 길 + B 따로 가는 길
# 플로이드 워셜 알고리즘을 사용한다.

def solution(n, s, a, b, fares):
    INF = 987654321
    # 2차원 최단거리 테이블 graph
    graph = [[INF]*(n+1) for _ in range(n+1)]
    
    # 자기 자신으로 가는 거리는 0으로 초기화
    for i in range(1,n+1):
        graph[i][i]=0
    
    # fares를 graph에 적용
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]
    # -- 여기까지 graph 초기화가 완성되었다.
      
    # 먼저 최단거리 테이블을 완성하자. 3중 for문을 사용한다. 여기서 시간을 너무 많이 잡아먹나?
    for v in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][v]+graph[v][j])
                
    
    return min(graph[s][v]+graph[v][a]+graph[v][b] for v in range(1,n+1))
