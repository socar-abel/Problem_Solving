import Foundation

let T = Int(readLine()!)!

for _ in 0..<T {
    program()
}


func program() {
    var answer = 0
    let arr = readLine()!.split(separator: " ").map{Int($0)!}
    let (N, M, K) = (arr[0], arr[1], arr[2])
    let arr2 = readLine()!.split(separator: " ").map{Int($0)!}
    let houses = arr2 + arr2[0..<M-1]
    var window = houses[0..<M].reduce(0){$0 + $1}
    if window < K {answer += 1}
    if N == M {
        print(answer)
        return
    }
    
    for i in M..<houses.count {
        window -= houses[i - M]
        window += houses[i]
        if window < K {answer += 1}
    }
    
    print(answer)
}

