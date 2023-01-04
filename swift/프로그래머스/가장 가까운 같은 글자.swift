import Foundation

func solution(_ s:String) -> [Int] {
    var result = [Int]()
    var alphaDict = [Character : Int]()
    
    for i in 0..<s.count {
        let x = s[s.index(s.startIndex, offsetBy: i)]
        if let val = alphaDict[x] {
            result.append(i - val)
        }
        else {
            result.append(-1)
        }
        alphaDict[x] = i
    }
    
    return result
}
