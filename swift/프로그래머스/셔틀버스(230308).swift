import Foundation

func toSecond(_ s: String) -> Int {
    let arr = s.components(separatedBy: ":")
    let (hour, minute) = (arr[0], arr[1])
    return Int(hour)! * 60 + Int(minute)!
}

func toString(_ x: Int) -> String {
    var hour = String(Int(x/60))
    var minute = String(Int(x%60))
    if hour.count < 2 {
        hour = "0" + hour
    }
    if minute.count < 2 {
        minute = "0" + minute
    }
    return hour + ":" + minute
}

func solution(_ n:Int, _ t:Int, _ m:Int, _ timetable:[String]) -> String {
    var answer = 0
    let busStart = 9*60
    let timetable = timetable.sorted(by: <)
    var readyQueue = Queue<Int>()
    for time in timetable {
        readyQueue.append(toSecond(time))
    }
    
    for i in 0..<n {
        let busTime = busStart + t*i
        if i == n-1 {
            var timeDict = [Int: Int]()
            var canRidePeople = 0
            while !readyQueue.isEmpty() && readyQueue.head()! <= busTime {
                let poped = readyQueue.pop()!
                timeDict[poped, default: 0] += 1
                canRidePeople += 1
            }

            if canRidePeople < m {
                answer = busTime
            }
            else {
                let first = timeDict.keys.min()!
                var tempTime = first - 1
                var tempTotal = 0
                while true {
                    if let people = timeDict[tempTime + 1] {
                        if tempTotal + people < m {
                            tempTime += 1
                            tempTotal += people
                        }
                        else {
                            break
                        }
                    }
                    else {
                        tempTime += 1
                    }
                }
                answer = tempTime
            }
        }
        else {
            for _ in 0..<m {
                if !readyQueue.isEmpty() {
                    if readyQueue.head()! <= busTime {
                        _ = readyQueue.pop()!
                    }
                    else {
                        break
                    }
                }
                else {
                    break
                }
            }
        }
    }
    
    
    return toString(answer)
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
