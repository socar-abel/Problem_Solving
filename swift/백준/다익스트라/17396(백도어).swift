import Foundation

struct Heap<T> {
    var list = [T]()
    var comparer : (T,T)->Bool
    init(comparer : @escaping (T,T)->Bool) {
        self.comparer = comparer
    }
    
    mutating func push(_ x : T) {
        var idx = list.count
        list.append(x)
        while idx > 0 , comparer(list[(idx-1)/2],list[idx]) {
            list.swapAt((idx-1)/2, idx)
            idx = (idx-1)/2
        }
    }
    mutating func pop() -> T? {
        if list.isEmpty { return nil }
        list.swapAt(0, list.count-1)
        let willDelete = list.removeLast()
        var idx = 0 , change = -1
        while idx < list.count {
            for k in idx*2+1...idx*2+2 {
                if k < list.count && comparer(list[idx],list[k]) {
                    if change == -1 || comparer(list[change],list[k]) {
                        change = k
                    }
                }
            }
            if change == -1 {break}
            list.swapAt(idx, change)
            idx = change
            change = -1
        }
        return willDelete
    }
    var isEmpty : Bool { return list.isEmpty}
}

extension Heap where T: Comparable {
    // 초기 설정을 해주지 않으면 Min Heap
    init() {
        self.init(comparer: >=)
    }
}

let INF = Int.max
let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
let ward = readLine()!.split(separator: " ").map{Int(String($0))!}
var graph = [[(Int, Int)]](repeating: [(Int, Int)](), count: N)
var distance = [Int](repeating: INF, count: N)

for _ in 0..<M {
    let temp = readLine()!.split(separator: " ").map{Int(String($0))!}
    graph[temp[0]].append((temp[1], temp[2]))
    graph[temp[1]].append((temp[0], temp[2]))
}

// 노드번호, 거리
var h = Heap<(Int, Int)>(comparer: { $0.1 >= $1.1 })
h.push((0, 0))
distance[0] = 0

while !h.isEmpty {
    let (x, dist) = h.pop()!
    
    if dist > distance[x] {
        continue
    }
    
    for (node, d) in graph[x] {
        if ward[node] == 1 && node != N - 1 {
            continue
        }
        let cost = dist + d
        if cost < distance[node] {
            h.push((node, cost))
            distance[node] = cost
        }
    }
}

print(distance.last == INF ? -1 : distance.last!)
