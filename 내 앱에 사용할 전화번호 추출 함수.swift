import Foundation

var recognizeResultElements: Array<String> = Array<String>(["0101", "훼이크", "080", "응 아니야", "080", "-", "123", "-", "4567"])

let consideredAsNumber: Array<Character> = Array<Character>(["o", "O", "ㅇ", "-", "."])
let confusingWithZero: Array<Character> = Array<Character>(["o", "O", "ㅇ"])

func isConsideredAsNumber(_ x: Character) -> Bool {
    if consideredAsNumber.contains(x) || x.isNumber {
        return true
    }
    else {
        return false
    }
}

func elemIsNumber(_ elem: String) -> Bool {
    var result: Bool = true
    for x in elem {
        if !isConsideredAsNumber(x) {
            result = false
            break
        }
    }
    return result
}

func refineElemNumber(_ number: String) -> String {
    var result: String = ""
    for x in number {
        if x.isNumber {
            result += String(x)
        }
        else if confusingWithZero.contains(x) {
            result += "0"
        }
    }
    return result
}

func getTELNumber(_ elements: Array<String>?) -> String? {
    guard let elements = elements else { return nil }
    var answer = ""
    for elem in elements {
        if elemIsNumber(elem) {
            answer += refineElemNumber(elem)
            
        }
        else {
            answer = ""
        }
        
        if 10 <= answer.count && answer.count <= 11 {
            break
        }
    }
    return answer
}

getTELNumber(recognizeResultElements)
