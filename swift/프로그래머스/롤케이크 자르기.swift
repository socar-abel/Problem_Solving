import Foundation

func solution(_ topping:[Int]) -> Int {
    var answer = 0
    var N = topping.count
    var dictA = [Int: Int]()
    var dictB = [Int: Int]()
    
    for t in topping {
        dictB[t, default: 0] += 1
    }
    
    for t in topping {
        dictA[t, default: 0] += 1
        guard dictB != nil else {
            continue
        }
        dictB[t]! -= 1
        if dictB[t]! == 0 {
            dictB[t] = nil
        }
        if dictA.count == dictB.count {
            answer += 1
        }
    }
    
    return answer
}
