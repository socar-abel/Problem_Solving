import Foundation

func solution(_ elements:[Int]) -> Int {
    let N = elements.count
    let elements = elements + elements
    var sumSet = Set<Int>()
    var prefixSum: [Int] = [0]
    
    for element in elements {
        let lastSum = prefixSum[prefixSum.endIndex-1]
        prefixSum.append(lastSum + element)
    }
    
    for i in 1...N {
        for j in 0..<N {
            sumSet.insert(prefixSum[j+i]-prefixSum[j])
        }
    }
    
    return sumSet.count
}

