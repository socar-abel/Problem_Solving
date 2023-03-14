func solution(_ msg:String) -> [Int] {
    var answer = [Int]()
    let N = msg.count
    var indexCount = 1
    var dict = [String: Int]()
    for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" {
        dict[String(x)] = indexCount
        indexCount += 1
    }
    
    var i = 0
    var tempInput = String(msg.first!)
    while i < N {
        // 가장 긴 입력 찾기
        while true {
            if i == N - 1 { break }
            let nextS = String(msg[msg.index(msg.startIndex, offsetBy: i + 1)])
            if dict[tempInput + nextS] == nil { break }
            tempInput += nextS
            i += 1
        }
        
        answer.append(dict[tempInput]!)
        if i < N - 1 {
            let nextS = String(msg[msg.index(msg.startIndex, offsetBy: i + 1)])
            dict[tempInput + nextS] = indexCount
            indexCount += 1
            tempInput = nextS
        }
        i += 1
    }

    return answer
}


