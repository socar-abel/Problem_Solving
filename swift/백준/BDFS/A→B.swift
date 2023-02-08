import Foundation

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


let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (A, B) = (input[0], input[1])
var answer = -1

var q = Queue<(Int, Int)>()
q.append((A, 1))

while !q.isEmpty() {
    let (x, cnt) = q.pop()!
    if x == B {
        answer = cnt
        break
    }
    if x * 2 <= B {
        q.append((x * 2, cnt + 1))
    }
    if 10 * x + 1 <= B {
        q.append((10 * x + 1, cnt + 1))
    }
}

print(answer)
