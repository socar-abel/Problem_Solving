import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var small = [Int]()
    var big = [Int]()
    
    for size in sizes {
        small.append(size.min()!)
        big.append(size.max()!)
    }

    return small.max()! * big.max()!
}
