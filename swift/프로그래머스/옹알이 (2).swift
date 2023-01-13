import Foundation

func solution(_ babbling:[String]) -> Int {
    var answer = 0
    let canSay = ["aya", "ye", "woo", "ma"]
    
    for b in babbling {
        var nowSay = b
        var tempSay = ""
        
        while true {
            var flag = false
            for say in canSay {
                if (nowSay.prefix(say.count) == say) && (tempSay != say) {
                    tempSay = say
                    nowSay.removeFirst(say.count)
                    flag = true
                    break
                }
            }
            
            if nowSay == "" {
                answer += 1
                break
            }
            if !(flag) {
                break
            }
        }
    }
    
    return answer
}

