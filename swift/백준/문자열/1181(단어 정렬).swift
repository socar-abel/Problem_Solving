import Foundation

let N = Int(readLine()!)!
var stringSet = Set<String>()

for _ in 0..<N {
    stringSet.insert(readLine()!)
}

var stringArr  = Array(stringSet)
stringArr.sort(by: {$0.count == $1.count ? $0 < $1 : $0.count < $1.count})
stringArr.forEach({print($0)})
