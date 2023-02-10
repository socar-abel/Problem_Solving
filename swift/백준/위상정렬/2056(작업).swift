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


let N = Int(readLine()!)!
var graph = [[Int]](repeating: [Int](), count: N + 1)
var time = [Int](repeating: 0, count: N + 1)
var inDegree = [Int](repeating: 0 , count: N + 1)
var tempTime = [[Int]](repeating: [Int](), count: N + 1)
var resultTime = [Int](repeating: 0, count: N + 1)

for i in 1...N {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    time[i] = input[0]
    for x in input[2..<input.count] {
        graph[x].append(i)
        inDegree[i] += 1
    }
}

// 노드번호, 시간
var q = Queue<(Int, Int)>()

for i in 1...N {
    if inDegree[i] == 0 {
        q.append((i, time[i]))
    }
}

while !q.isEmpty() {
    let (x, t) = q.pop()!
    resultTime[x] = t
    
    for next in graph[x] {
        inDegree[next] -= 1
        tempTime[next].append(t)
        if inDegree[next] == 0 {
            q.append((next, tempTime[next].max()! + time[next]))
        }
    }
}

print(resultTime.max()!)
