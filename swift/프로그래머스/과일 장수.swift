import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    var answer = 0
    let s = score.sorted()
    let startIndex = (score.count) % m
    var tempBox = [Int]()
    
    for i in (startIndex)..<s.count {
        tempBox.append(s[s.index(s.startIndex, offsetBy: i)])
        if tempBox.count == m {
            answer += tempBox[0] * m
            tempBox = [Int]()
        }
    }
    
    return answer
}
