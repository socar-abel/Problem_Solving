import Foundation

final class IO {
    private let buffer:[UInt8]
    private var index: Int = 0

    init(fileHandle: FileHandle = FileHandle.standardInput) {

        buffer = Array(try! fileHandle.readToEnd()!)+[UInt8(0)] // 인덱스 범위 넘어가는 것 방지
    }

    @inline(__always) private func read() -> UInt8 {
        defer { index += 1 }

        return buffer[index]
    }

    @inline(__always) func readInt() -> Int {
        var sum = 0
        var now = read()
        var isPositive = true

        while now == 10
                      || now == 32 { now = read() } // 공백과 줄바꿈 무시
        if now == 45 { isPositive.toggle(); now = read() } // 음수 처리
        while now >= 48, now <= 57 {
            sum = sum * 10 + Int(now-48)
            now = read()
        }

        return sum * (isPositive ? 1:-1)
    }

    @inline(__always) func readString() -> String {
        var now = read()

        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시
        let beginIndex = index-1

        while now != 10,
              now != 32,
              now != 0 { now = read() }

        return String(bytes: Array(buffer[beginIndex..<(index-1)]), encoding: .ascii)!
    }

    @inline(__always) func readByteSequenceWithoutSpaceAndLineFeed() -> [UInt8] {
        var now = read()

        while now == 10 || now == 32 { now = read() } // 공백과 줄바꿈 무시
        let beginIndex = index-1

        while now != 10,
              now != 32,
              now != 0 { now = read() }

        return Array(buffer[beginIndex..<(index-1)])
    }

    @inline(__always) func writeByString(_ output: String) { // wapas
        FileHandle.standardOutput.write(output.data(using: .utf8)!)
    }
}

let io = IO()

var T = io.readInt()
var t = 1
var parent = [Int]()

func findParent(_ x: Int) -> Int {
    if parent[x] == x {
        return x
    }
    parent[x] = findParent(parent[x])
    return parent[x]
}

func union(_ x: Int, _ y: Int) {
    let px = findParent(x)
    let py = findParent(y)
    parent[max(px, py)] = parent[min(px, py)]
}

func program() {
    let N = io.readInt()
    let K = io.readInt()
    var answers = [Int]()

    parent = [Int](repeating: 0, count: N)
    for i in 0..<N {
        parent[i] = i
    }

    for _ in 0..<K {
        let (x, y) = (io.readInt(), io.readInt())
        union(x, y)
    }

    let M = io.readInt()
    for _ in 0..<M {
        let (x, y) = (io.readInt(), io.readInt())
        answers.append(findParent(x) == findParent(y) ? 1 : 0)
    }

    print("Scenario \(t):")
    for answer in answers {
        print(answer)
    }
    print()
}

while t <= T {
    program()
    t += 1
}
