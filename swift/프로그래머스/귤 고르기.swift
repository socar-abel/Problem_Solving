import Foundation

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    let N = tangerine.count
    var weight = [Int: Int]()
    
    for t in tangerine {
        weight[t, default: 0] += 1
    }
    
    var weightKey = Array(weight.keys)
    weightKey.sort(by: { weight[$0]! < weight[$1]! })
    
    var i = N - k
    while i > 0 {
        for key in weightKey {
            if i >= weight[key]! {
                i -= weight[key]!
                weight[key] = nil
            }
            else {
                i = 0
                weight[key]! -= i
                if weight[key] == 0 {
                    weight[key] = nil
                }
            }
        }
    }
    
    return weight.count
}
