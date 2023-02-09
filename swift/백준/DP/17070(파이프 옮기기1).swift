import Foundation

let N = Int(readLine()!)!
var graph = [[Int]](repeating: [Int](), count: N)
var dp = [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: -1, count: 3), count: N), count: N)

for i in 0..<N {
    graph[i] = readLine()!.split(separator: " ").map{Int(String($0))!}
}

func dfs(x: Int, y: Int, d: Int) -> Int {
    if dp[x][y][d] != -1 {
        return dp[x][y][d]
    }
    if (x, y) == (N - 1, N - 1) {
        dp[x][y][d] = 1
        return 1
    }

    dp[x][y][d] = 0

    if d == 0 {
        if y + 1 < N && graph[x][y + 1] == 0 {
            dp[x][y][d] += dfs(x: x, y: y + 1, d: 0)
        }
    }
    else if d == 1 {
        if x + 1 < N && graph[x + 1][y] == 0 {
            dp[x][y][d] += dfs(x: x + 1, y: y, d: 1)
        }
    }
    else if d == 2 {
        if y + 1 < N && graph[x][y + 1] == 0 {
            dp[x][y][d] += dfs(x: x, y: y + 1, d: 0)
        }
        if x + 1 < N && graph[x + 1][y] == 0 {
            dp[x][y][d] += dfs(x: x + 1, y: y, d: 1)
        }
    }

    if x + 1 < N && y + 1 < N &&
        graph[x][y + 1] == 0 && graph[x + 1][y] == 0 && graph[x + 1][y + 1] == 0 {
        dp[x][y][d] += dfs(x: x + 1, y: y + 1, d: 2)
    }

    return dp[x][y][d]
}


let answer = dfs(x: 0, y: 1, d: 0)
print(answer)

