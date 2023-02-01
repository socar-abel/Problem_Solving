import Foundation

func solution(_ k:Int, _ d:Int) -> Int64 {
    var answer: Int = 0

    for x in stride(from: 0, to: d+1, by: k) {
        let floor = (sqrt(pow(Double(d), 2) - pow(Double(x), 2)))
        answer += Int(floor/Double(k)) + 1
    }

    return Int64(answer)
}
