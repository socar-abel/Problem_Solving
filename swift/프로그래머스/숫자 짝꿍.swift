import Foundation

func solution(_ X:String, _ Y:String) -> String {
    var answer = ""
    var xDict = [Character : Int]()
    var yDict = [Character : Int]()
    var xyDict = [Character : Int]()
    
    for x in X {
        xDict[x, default: 0] += 1
    }
    
    for y in Y {
        yDict[y, default: 0] += 1
    }
    
    for n in xDict.keys {
        if yDict[n] != nil {
            xyDict[n] = min(xDict[n]!, yDict[n]!)
        }
    }
    
    print(xyDict)
    if xyDict.isEmpty {
        answer = "-1"
    }
    else {
        if xyDict["0"] != nil && xyDict.count == 1 {
            answer = "0"
        }
        else {
            for n in xyDict.keys.sorted(by: >) {
                answer += String(repeating: n, count: xyDict[n]!)
            }
        }
    }
    
    return answer
}
