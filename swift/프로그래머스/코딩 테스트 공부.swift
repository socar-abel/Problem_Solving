import Foundation

func solution(_ alp:Int, _ cop:Int, _ problems:[[Int]]) -> Int {
    let INF = 987654321
    var answer = INF
    let maxAlp = problems.map{$0[0]}.max()!
    let maxCop = problems.map{$0[1]}.max()!
    var dp = [[Int]](repeating: [Int](repeating: INF, count: 151), count: 151)
    dp[alp][cop] = 0
    
    for i in alp...150 {
        for j in cop...150 {
            if j < 150 {
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            }
            if i < 150 {
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)    
            }
            
            for problem in problems {
                if i >= problem[0] && j >= problem[1] {
                    let ni = min(150, i + problem[2])
                    let nj = min(150, j + problem[3])
                    dp[ni][nj] = min(dp[ni][nj], dp[i][j] + problem[4])
                }
            }
        }
    }

    for i in maxAlp...150 {
        for j in maxCop...150 {
            answer = min(answer, dp[i][j])
        }
    }

    return answer
}


