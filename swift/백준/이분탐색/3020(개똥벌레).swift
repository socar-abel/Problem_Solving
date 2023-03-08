import Foundation

let arr = readLine()!.split(separator: " ")
let (N, H) = (Int(arr[0])!, Int(arr[1])!)
var sky = [Int]()
var ground = [Int]()
var breakDict = [Int: Int]()

for i in 0..<N {
    if i % 2 == 0 {
        ground.append(Int(readLine()!)!)
    }
    else {
        sky.append((Int(readLine()!)!))
    }
}

sky.sort(by: <)
ground.sort(by: <)


for h in 1...H {
    var gLeft = 0
    var gRight = ground.count - 1
    // h 에서 부딪히는 최소 인덱스
    var gIndex = 0
    // 높이가 h 일때 파괴하는 장애물 개수
    var gAnswer = 0
    
    while (gLeft <= gRight) {
        let mid = Int((gLeft + gRight)/2)
        if h <= ground[mid] {
            gIndex = mid
            gRight = mid - 1
        }
        else {
            gLeft = mid + 1
        }
    }
    
    if gIndex == 0 && ground.last! < h {
        gAnswer = 0
    }
    else {
        gAnswer = ground.count - gIndex
    }
    
    var sLeft = 0
    var sRight = sky.count - 1
    // h 에서 부딪히는 최소 인덱스
    var sIndex = 0
    // 높이가 h 일때 파괴하는 장애물 개수
    var sAnswer = 0
    
    while (sLeft <= sRight) {
        let mid = Int((sLeft + sRight)/2)
        if H - sky[mid] < h {
            sIndex = mid
            sRight = mid - 1
        }
        else {
            sLeft = mid + 1
        }
    }
    
    if sIndex == 0 && H - sky.last! >= h{
        sAnswer = 0
    }
    else {
        sAnswer = sky.count - sIndex
    }
    
    breakDict[h] = gAnswer + sAnswer
    
}

var count = 0
let minValue = breakDict.values.min()!
for key in breakDict.keys {
    if breakDict[key]! == minValue {
        count += 1
    }
}

print("\(minValue) \(count)")
