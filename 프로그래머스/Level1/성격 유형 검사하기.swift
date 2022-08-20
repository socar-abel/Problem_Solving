import Foundation

func solution(_ survey:[String], _ choices:[Int]) -> String {
    var typeDict = [String : Int]()
    
    for i in 0 ..< survey.count {
        if let result = getTypeScore(survey[i], choices[i]) {
            let a = result.a , b = result.b
            if typeDict[a] != nil {
                typeDict[a]! += b
            }
            else {
                typeDict[a] = b
            }
        }
    }

    return getResult(dict: &typeDict)
}


func getTypeScore(_ type: String, _ score: Int) -> (a: String, b: Int)? {
    
    let first = String(type.first!)
    let second = String(type.last!)
    
    switch score {
        case 1:
            return (first, 3)
        case 2:
            return (first, 2)
        case 3:
            return (first, 1)
        case 4:
            return nil
        case 5:
            return (second, 1)
        case 6:
            return (second, 2)
        case 7:
            return (second, 3)
        default:
            return nil
    }
}

func getResult(dict: inout [String : Int]) -> String {
    var result = ""
    
    for type in ["R", "T", "C", "F", "J", "M", "A", "N"] {
        if dict[type] == nil {
            dict[type] = 0
        }
    }
    
    dict["R"]! >= dict["T"]! ? result.append("R") : result.append("T")
    dict["C"]! >= dict["F"]! ? result.append("C") : result.append("F")
    dict["J"]! >= dict["M"]! ? result.append("J") : result.append("M")
    dict["A"]! >= dict["N"]! ? result.append("A") : result.append("N")
    
    print("result = \(result)")
    
    return result
}

