def solution(alp, cop, problems):
    INF = 987654321
    answer = INF
    dp = [[INF]*151 for _ in range(151)]
    dp[alp][cop] = 0
    problems.append([0, 0, 1, 0, 1])
    problems.append([0, 0, 0, 1, 1])
    max_alp = max(problems, key=lambda x: x[0])[0]
    max_cop = max(problems, key=lambda x: x[1])[1]
    
    for i in range(alp, 151):
        for j in range(cop, 151):
            for problem in problems:
                # 풀 수 있는 문제이면
                if i >= problem[0] and j >= problem[1]:
                    ni = min(150, i + problem[2])
                    nj = min(150, j + problem[3])
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + problem[4])
    
    for i in range(max_alp, 151):
        for j in range(max_cop, 151):
            answer = min(answer, dp[i][j])
    
    return answer
