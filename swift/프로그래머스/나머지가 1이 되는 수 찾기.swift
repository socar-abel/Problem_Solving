import Foundation

func solution(_ n:Int) -> Int {
    var answer = 0
    for x in 1..<n {
        if n % x == 1 {
            answer = x
            break
        }
    }
    return answer
}

