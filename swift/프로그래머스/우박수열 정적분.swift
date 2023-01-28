// 개선하기 전 정답 코드
//import Foundation
//
//func getArea(_ x1: Int, _ x2: Int, _ y1: Int, _ y2: Int) -> Double {
//    let dx: Double = Double(x2 - x1)
//    let dy: Double = Double(max(y1, y2) - min(y1, y2))
//    let sqaure: Double = dx * Double(min(y1, y2))
//    let triangle: Double = dx * dy * (0.5)
//    return sqaure + triangle
//}
//
//func solution(_ k:Int, _ ranges:[[Int]]) -> [Double] {
//    var answer = [Double]()
//    var intervalArea: [Double] = [0.0]
//    var arr: [Int] = [k]
//    var n = k
//
//    while n != 1 {
//        if n % 2 == 0 {
//            n /= 2
//        }
//        else {
//            n *= 3
//            n += 1
//        }
//        arr.append(n)
//    }
//
//    // [0-0, 0-1, 0-2, ... 0-5] (N = 6)
//    for i in 0..<arr.count-1 {
//        let tempArea = getArea(i, i+1, arr[i], arr[i+1])
//        intervalArea.append(intervalArea.last! + tempArea)
//    }
//
//    let lastX = arr.count - 1
//    for range in ranges {
//        let x1 = range[0]
//        let x2 = lastX + range[1]
//
//        if x1 == x2 {
//            answer.append(0)
//        }
//        else if x1 > x2 {
//            answer.append(-1)
//        }
//        else {
//            answer.append(intervalArea[x2] - intervalArea[x1])
//        }
//    }
//
//    return answer
//}

// 개선 후 정답 코드
import Foundation

func getArea(_ x1: Int, _ x2: Int, _ y1: Int, _ y2: Int) -> Double {
    let dx: Double = Double(x2 - x1)
    let dy: Double = Double(max(y1, y2) - min(y1, y2))
    let sqaure: Double = dx * Double(min(y1, y2))
    let triangle: Double = dx * dy * (0.5)
    return sqaure + triangle
}
    
func solution(_ k:Int, _ ranges:[[Int]]) -> [Double] {
    var answer = [Double]()
    var intervalArea: [Double] = [0.0]
    var arr: [Int] = [k]
    var n = k
    
    while n != 1 {
        n = n % 2 == 0 ? n/2 : n*3 + 1
        arr.append(n)
    }
 
    // [0-0, 0-1, 0-2, ... 0-5] (N = 6)
    for i in 0..<arr.count-1 {
        let tempArea = getArea(i, i+1, arr[i], arr[i+1])
        intervalArea.append(intervalArea.last! + tempArea)
    }

    let lastX = arr.count - 1
    
    return ranges.map { range in
        let (a, b) = (range[0], lastX + range[1])
        return a > b ? -1 : intervalArea[b] - intervalArea[a]
    }
}


