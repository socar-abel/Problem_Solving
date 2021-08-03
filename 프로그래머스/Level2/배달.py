def solution(N, road, K):
    answer = 0
    INF = 987654321
    
    table = [[INF] * (N+1) for _ in range(N+1)]
    for a in range(1,N+1):
        table[a][a] = 0
    for r in road:
        table[r[0]][r[1]] = min(table[r[0]][r[1]], r[2])
        table[r[1]][r[0]] = min(table[r[1]][r[0]], r[2])

    for k in range(1,N+1):
        for a in range(1,N+1):
            for b in range(1,N+1):
                table[a][b] = min(table[a][b], table[a][k] + table[k][b])
    
    for i in range(1,N+1):
        if table[1][i] <= K : answer += 1
    
    return answer
