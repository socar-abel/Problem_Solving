import Foundation

let N = Int(readLine()!)!

for i in 1...N
{
    for j in 1...i
    {
        print("*", terminator: "")
    }
    print()
}
