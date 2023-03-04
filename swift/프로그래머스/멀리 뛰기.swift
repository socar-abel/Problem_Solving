import Foundation

func solution(_ n:Int) -> Int {
    var dp = [Int](repeating: 0, count: n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in 2..<n+1 {
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    }
    
    return dp.last!
}
