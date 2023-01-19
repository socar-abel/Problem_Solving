import Foundation

func solution(_ numbers:[Int]) -> Int {
    return (0...9).filter({!(numbers.contains($0))}).reduce(0, +)
}
