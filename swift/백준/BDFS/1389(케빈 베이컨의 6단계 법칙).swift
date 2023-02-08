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
let (N, M) = (input[0], input[1])
var graph = [[Int]](repeating: [Int](), count: (N+1))
var kevinValues = [Int](repeating: 987654321, count: (N+1))

for _ in 0..<M {
    let friend = readLine()!.split(separator: " ").map{Int(String($0))!}
    graph[friend[0]].append(friend[1])
    graph[friend[1]].append(friend[0])
}

for i in 1...N {
    var tempKevinValue = 0
    var visit = [Bool](repeating: false, count: N+1)
    var q = Queue<(Int, Int)>()
    q.append((i, 0))
    visit[i] = true
    
    while !q.isEmpty() {
        let (x, cnt) = q.pop()!
        
        for node in graph[x] {
            if !visit[node] {
                q.append((node, cnt + 1))
                visit[node] = true
                tempKevinValue += cnt + 1
            }
        }
    }
    
    kevinValues[i] = tempKevinValue
}

let minKevinValue = kevinValues.min()!
print(kevinValues.firstIndex(of: minKevinValue)!)
