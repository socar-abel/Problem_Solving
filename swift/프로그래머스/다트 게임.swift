func solution(_ dartResult:String) -> Int {
    var darts = [String]()
    var scores = [Int](repeating: 0, count: 3)
    
    var tempString = ""
    for i in 0..<dartResult.count {
        let index = dartResult.index(dartResult.startIndex, offsetBy: i)
        let s = dartResult[index]
        if i == 0 {
            tempString += String(s)
            continue
        }
        if s == "0" {
            if tempString == "1" {
                tempString += String(s)
            }
            else {
                darts.append(tempString)
                tempString = String(s)
            }
        }
        else if "123456789".contains(s) {
            darts.append(tempString)
            tempString = String(s)
        }
        else {
            tempString += String(s)
        }
    }
    darts.append(tempString)

    // ["1D", "2S#", "10S"]
    for i in 0..<darts.count {
        let dart = darts[i]
        var num = ""
        var SDT = ""
        var option = ""
        
        for s in dart {
            if "0123456789".contains(s) {
                num += String(s)
            }
            else if "SDT".contains(s) {
                SDT = String(s)
            }
            else if "*#".contains(s) {
                option = String(s)
            }
        }
        
        scores[i] = Int(num)!
        if SDT == "D" { scores[i] = scores[i] * scores[i] }
        else if SDT == "T" { scores[i] = scores[i] * scores[i] * scores[i] }
        if option == "*" {
            scores[i] *= 2
            if i >= 1 { scores[i-1] *= 2 }
        }
        else if option == "#" {
            scores[i] *= (-1)
        }
        
    }
    
    return scores.reduce(0) { $0 + $1 }
}
