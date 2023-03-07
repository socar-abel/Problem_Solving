import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var answer = 0
    let N = board.count
    var boardStack = [[Int]](repeating: [Int](), count: N)
    var mainStack = [Int]()
    
    for i in (0..<N).reversed() {
        for j in 0..<N {
            if board[i][j] == 0 { continue }
            boardStack[j].append(board[i][j])
        }
    }
    
    for move in moves {
        let m = move - 1
        if !boardStack[m].isEmpty {
            let poped = boardStack[m].popLast()!
            if let top = mainStack.last, top == poped {
                let _ = mainStack.popLast()
                answer += 2
            }
            else {
                mainStack.append(poped)
            }
        }
    }
    
    return answer
}
