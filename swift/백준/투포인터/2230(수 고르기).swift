import Foundation

let input = readLine()!.split{$0==" "}.map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var arr = [Int]()
var answer = Int.max

for _ in 0..<N {
    arr.append(Int(readLine()!)!)
}

arr.sort(by: <)

var r = 1
for l in 0..<N {
    while r < N && arr[r] - arr[l] < M {
        r += 1
    }
    if r < N && arr[r] - arr[l] >= M {
        answer = min(answer, arr[r] - arr[l])
    }
}

print(answer)
