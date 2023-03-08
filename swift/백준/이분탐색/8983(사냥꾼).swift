import Foundation

var answer = 0
let arr = readLine()!.split(separator: " ").map{Int($0)!}
let (M, N, L) = (arr[0], arr[1], arr[2])
var animals = [(x: Int, y: Int)]()
var hunters = Array(readLine()!.split(separator: " ").map{Int($0)!})
hunters.sort(by: <)

for _ in 0..<N {
    let input = readLine()!.split(separator: " ").map{Int($0)!}
    animals.append((input[0], input[1]))
}


// O(N)
for (x, y) in animals {
    // 이진탐색으로 x와 가장 가까운 사대 인덱스 탐색
    var left = 0
    var right = M-1
    var nearLeft = -1
    var nearRight = -1
    var same = -1
    
    while (left <= right) {
        let mid = Int((left + right)/2)
        if hunters[mid] == x {
            same = mid
            break
        }
        else if hunters[mid] < x {
            left = mid + 1
            nearLeft = mid
        }
        else {
            right = mid - 1
            nearRight = mid
        }
    }
    
    if same != -1 {
        if y <= L {
            answer += 1
        }
    }
    else {
        if nearLeft != -1 && x - hunters[nearLeft] + y <= L {
            answer += 1
        }
        else if nearRight != -1 && hunters[nearRight] - x + y <= L {
            answer += 1
        }
    }
}

print(answer)
