import Foundation

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    var answer = 0
    
    for i in 1...number {
        var tempCount = 0
        var flag = true
        for j in 1...Int(sqrt(Double(i))) {
            if i % j == 0 {
                if j * j == i {
                    tempCount += 1
                }
                else {
                    tempCount += 2
                }
            }
            if tempCount > limit {
                flag = false
                break
            }
        }
        
        if flag {
            answer += tempCount
        }
        else {
            answer += power
        }
    }
    
    return answer
}
