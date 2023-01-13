import Foundation

func solution(_ food:[Int]) -> String {
    var answer = ""
    
    for (idx, value) in food.map({$0 / 2}).enumerated() {
        answer += String(repeating: String(idx), count: value)
    }
    
    answer += "0" + String(answer.reversed())
    
    return answer
}

