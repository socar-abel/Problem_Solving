import Foundation

func solution(_ want:[String], _ number:[Int], _ discount:[String]) -> Int {
    var answer = 0
    var wantDict = [String : Int]()
    var windowDict = [String : Int]()
    
    for i in 0..<want.count {
        wantDict[want[i]] = number[i]
    }
    
    for i in 0..<10 {
        windowDict[discount[i], default: 0] += 1
    }
    
    if windowDict == wantDict {
        answer += 1
    }
    
    for i in 0..<discount.count-10 {
        windowDict[discount[i]]! -= 1
        if windowDict[discount[i]]! == 0 {
            windowDict[discount[i]] = nil
        }
        windowDict[discount[i+10], default: 0] += 1
        
        if windowDict == wantDict {
            answer += 1
        }
    }
    
    return answer
}
