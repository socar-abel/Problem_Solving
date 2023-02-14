import Foundation

func solution(_ weights:[Int]) -> Int64 {
    var answer: Int64 = 0
    var dict = [Int: Int]()
    let ratio: [(Int, Int)] = [(1, 2), (2, 3), (3, 4)]
    weights.forEach{ dict[$0, default: 0] += 1 }
    
    for w in dict.keys {
        let x: Int = Int(dict[w]!)
        answer += Int64((x * (x-1))/2)
        for (a, b) in ratio {
            let y = Int(Double(w) * Double(a)/Double(b))
            if w % b == 0 && dict[y] != nil {
                answer += Int64(x * dict[y]!)
            }
        }
    }
    
    return answer
}
