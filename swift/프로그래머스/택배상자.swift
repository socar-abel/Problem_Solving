import Foundation

func solution(_ order:[Int]) -> Int {
    let N = order.count
    var stack = [Int]()
    var tempN = 1
    var answer = 0

    for want in order {
        if !stack.isEmpty && stack[stack.endIndex-1] == want {
            _ = stack.popLast()
            answer += 1
            continue
        }
        else {
            while tempN <= N && want != tempN {
                stack.append(tempN)
                tempN += 1
            }
            if tempN > N {
                break
            }
            answer += 1
            tempN += 1
        }
    }

    return answer
}
