import Foundation

func solution(_ users:[[Int]], _ emoticons:[Int]) -> [Int] {
    var answer = [0, 0]
    let N = users.count
    let M = emoticons.count
    var discountCases = [[Int]]()

    var q = Queue<[Int]>()
    for rate in [10, 20, 30, 40] {
        q.append([rate])
    }
    
    while !q.isEmpty() {
        let now = q.pop()!
        
        if now.count == M {
            discountCases.append(now)
            continue
        }
        
        for rate in [10, 20, 30, 40] {
            q.append(now + [rate])
        }
    }
    
    for discountCase in discountCases {
        var tempJoinUser = 0
        var tempTotalPrice:Float = 0
        
        for user in users {
            var tempUserPrice: Float = 0
            
            for i in 0..<M {
                if user[0] <= discountCase[i] {
                    tempUserPrice += Float(emoticons[i]) * (1.0 - Float(discountCase[i])/Float(100))
                }
            }
            
            if Float(user[1]) <= tempUserPrice {
                tempJoinUser += 1
            }
            else {
                tempTotalPrice += tempUserPrice
            }
        }
        if answer[0] < tempJoinUser {
            answer[0] = tempJoinUser
            answer[1] = Int(tempTotalPrice)
        }
        else if answer[0] == tempJoinUser && answer[1] < Int(tempTotalPrice) {
            answer[1] = Int(tempTotalPrice)
        }
    }
    
    return answer
}

struct Queue<T> {
    var inputStack = [T]()
    var outputStack = [T]()
    
    mutating func append(_ x: T) {
        inputStack.append(x)
    }
    
    mutating func pop() -> T? {
        var top: T?
        if outputStack.isEmpty {
            outputStack = inputStack.reversed()
            inputStack.removeAll()
            top = outputStack.popLast()
        }
        else {
            top = outputStack.popLast()
        }
        return top
    }
    
    mutating func head() -> T? {
        if outputStack.isEmpty {
            outputStack = inputStack.reversed()
            inputStack.removeAll()
        }
        return outputStack.isEmpty ? nil : outputStack[outputStack.endIndex-1]
    }
    
    func isEmpty() -> Bool {
        return inputStack.isEmpty && outputStack.isEmpty ? true : false
    }
}

