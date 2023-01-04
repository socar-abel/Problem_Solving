import Foundation

func solution(_ t:String, _ p:String) -> Int {
    var result = 0
    
    for i in 0...(t.count - p.count) {
        let subString = t.dropFirst(i).prefix(p.count)
        if let temp = Int(subString), let intP = Int(p) {
            result += temp <= intP ? 1 : 0
        }
    }

    return result
}

