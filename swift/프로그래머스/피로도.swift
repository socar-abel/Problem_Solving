import Foundation

func solution(_ k:Int, _ dungeons:[[Int]]) -> Int {
    var answer = 0
    let dungeonsCount = dungeons.count
    
    for permutation in permuteWirth(Array(0..<dungeonsCount), dungeonsCount-1) {
        var tempK = k
        var tempAnswer = 0
        for now in permutation {
            let (minEnergy, useEnergy) = (dungeons[now][0], dungeons[now][1])
            if minEnergy <= tempK {
                tempK -= useEnergy
                tempAnswer += 1
            }
            else {
                break
            }
        }
        answer = max(answer, tempAnswer)
    }
    
    return answer
}

func permuteWirth<T>(_ a: [T], _ n: Int) -> [[T]] {
    if n == 0 {
        return [a]
    }
    var a = a
    var ret = permuteWirth(a, n - 1)
    for i in 0..<n {
        a.swapAt(i, n)
        ret += permuteWirth(a, n - 1)
        a.swapAt(i, n)
    }
    return ret
}
