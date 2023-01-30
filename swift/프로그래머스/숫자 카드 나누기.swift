import Foundation

func isSatisfied(_ arrayA:[Int], _ arrayB:[Int], _ x: Int) -> Bool {
    var setA = Set<Bool>()
    var setB = Set<Bool>()
    
    for a in arrayA {
        setA.insert(a % x == 0 ? true : false)
    }
    
    for b in arrayB {
        setB.insert(b % x == 0 ? true : false)
    }
    
    return ((setA.count == 1) && (setB.count == 1) && (setA != setB)) ? true : false
}

func getGCD(_ a: Int, _ b: Int) -> Int {
    return a == 0 ? b : getGCD(b % a, a)
}

func solution(_ arrayA:[Int], _ arrayB:[Int]) -> Int {
    var answer = 0
    let gcdA = arrayA.reduce(arrayA.first!) { getGCD($0, $1) }
    let gcdB = arrayB.reduce(arrayB.first!) { getGCD($0, $1) }
    if isSatisfied(arrayA, arrayB, gcdA) {
        answer = max(answer, gcdA)
    }
    if isSatisfied(arrayA, arrayB, gcdB) {
        answer = max(answer, gcdB)
    }
    
    return answer
}
