import Foundation

func solution(_ storey:Int) -> Int {
    var answer = 0
    var arr = String(storey).map{Int(String($0))!}
    arr.reverse()
    
    for i in 0..<arr.count {
        if arr[i] < 5 {
            answer += arr[i]
        }
        else if arr[i] == 5 {
            if i + 1 < arr.count {
                if arr[i + 1] >= 5 {
                    arr[i + 1] += 1
                }
            }
            answer += 5
        }
        else {
            (i + 1 < arr.count) ? (arr[i + 1] += 1) : (answer += 1)
            answer += (10 - arr[i])
        }
    }
    
    return answer
}
