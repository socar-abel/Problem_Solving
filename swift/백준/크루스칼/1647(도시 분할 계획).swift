import Foundation

let input = readLine()!.split{$0==" "}.map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var edges = [(Int, Int, Int)]()
var parent = [Int](repeating: 0, count: N + 1)
for i in 0...N {
    parent[i] = i
}

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
    parent[max(px, py)] = min(px, py)
}

for _ in 0..<M {
    let input2 = readLine()!.split{$0==" "}.map{Int(String($0))!}
    edges.append((input2[0], input2[1], input2[2]))
}

edges.sort{$0.2 < $1.2}
var edgeCount = 0
var answer = 0

for (a, b, c) in edges {
    if findParent(a) != findParent(b) {
        union(a, b)
        edgeCount += 1
        answer += c
    }
    if edgeCount == N - 2 {
        break
    }
}

print(answer)
