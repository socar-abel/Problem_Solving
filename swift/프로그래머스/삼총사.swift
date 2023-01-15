import Foundation

func solution(_ number:[Int]) -> Int {
    var answer = 0
    // 5명일 때
    // (1, 2, 3), (1, 2, 4), (1, 2, 5)
    // (2, 3, 4), (2, 3, 5) ...
    for i in 0..<number.count {
        for j in i+1..<number.count {
            for k in j+1..<number.count {
                if number[i] + number[j] + number[k] == 0 {
                    answer += 1
                }
            }
        }
    }
    
    return answer
}
