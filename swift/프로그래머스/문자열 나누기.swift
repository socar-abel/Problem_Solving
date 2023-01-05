import Foundation

func solution(_ s:String) -> Int {
    var result = 0
    var tempX: Character? = nil
    var tempXCount = 0
    var tempNotXCount = 0
    
    for i in 0..<s.count {
        if i == s.count - 1 {
            result += 1
            break
        }
        if tempX == nil {
            tempX = s[s.index(s.startIndex, offsetBy: i)]
            tempXCount += 1
            continue
        }
        if s[s.index(s.startIndex, offsetBy: i)] == tempX {
            tempXCount += 1
        }
        else {
            tempNotXCount += 1
        }
        if tempXCount == tempNotXCount {
            result += 1
            tempX = nil
        }
    }
    
    return result
}
