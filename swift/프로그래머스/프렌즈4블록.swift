import Foundation

// m 높이 n 폭
func solution(_ m:Int, _ n:Int, _ board:[String]) -> Int {
    var answer = 0
    let direction = [(0, 1), (1, 0), (1, 1)]
    var graph = [[String]]()
    
    for s in board {
        var tempArr = [String]()
        for x in s {
            tempArr.append(String(x))
        }
        graph.append(tempArr)
    }
    
    while true {
        // 이 판에 깨지는게 하나라도 있는지
        var flag = false
        var breakList = [(Int, Int)]()

        for x in 0..<m {
            for y in 0..<n {
                if graph[x][y] == "XX" { continue }
                var canBreak = true

                for d in direction {
                    let nx = x + d.0
                    let ny = y + d.1

                    if !(nx < m && ny < n && graph[x][y] == graph[nx][ny]) {
                        canBreak = false
                        break
                    }
                }

                if canBreak {
                    flag = true
                    breakList.append((x, y))
                    for d in direction {
                        breakList.append((x + d.0, y + d.1))
                    }
                }
            }
        }
        
        if !flag { break }
        
        for (i, j) in breakList {
            graph[i][j] = "XX"
        }

        var columns = [[String]](repeating: [String](), count: n)
        for i in (0..<m).reversed() {
            for j in 0..<n {
                if graph[i][j] == "XX" { continue }
                columns[j].append(graph[i][j])
            }
        }
        
        for j in 0..<n {
            for i in 0..<m {
                if i < columns[j].count {
                    graph[m-1-i][j] = columns[j][i]
                }
                else {
                    graph[m-1-i][j] = "XX"
                }
            }
        }
        
    }
    
    for g in graph {
        answer += g.filter{$0 == "XX"}.count
    }
    
    return answer
}
