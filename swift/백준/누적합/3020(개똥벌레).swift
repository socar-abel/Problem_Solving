import Foundation

let arr = readLine()!.split(separator: " ").map{Int($0)!}
let (N, H) = (arr[0], arr[1])

// bottom[h] = x  (높이 h에서 딱 끝나는 장애물이 x 개라는 뜻.)
// top[h] = y     (높이 h에서 딱 끝나는 장애물이 y 개라는 뜻.)

// 예를들어 H = 7 일 때,
// bottom[2] = 4 (높이 h = 2 에서 끝나는 장애물이 4개 있다)
// top[5] = 3 (높이 7 - 5 + 1 = 3 에서 끝나는 장애물이 2개 있다)
var top = [Int](repeating: 0, count: H+1)
var bottom = [Int](repeating: 0, count: H+1)

for i in 0..<N {
    if i % 2 == 0 {
        bottom[Int(readLine()!)!] += 1
    }
    else {
        top[H-Int(readLine()!)!+1] += 1
    }
}

// 이제 누적합을 구할거다. 왜, 어떻게 누적합을 구하느냐.
// bottom[x] 에는 높이 h = x 에서 끝나는 장애물의 개수가 담겨있다.

// 예를 들어, ... bottom[5] = 1, bottom[6] = 0, bottom[7] = 1 이라고 해보자.

// 높이 7에서 끝나는 장애물이 1개 있으므로, 그 장애물은 높이 6에서도 무조건 부딪힌다.
// 그렇기 때문에 bottom[7] 의 값을 bottom[6] 에 더해주면,
// h = 6 에서 부딪히는 장애물의 개수를 구할 수 있게 된다.
// 더한 결과 : bottom[6] = 1  (높이 6에서는 부딪히는 장애물이 1개라는 뜻)

// 6, 7 의 누적합을 5에도 더해준다. bottom[5] = 2
// 높이 5에서 부딪히는 장애물은 2개라는 걸 알게 된다.

for h in (0...H) {
    if H-h-1 >= 0 {
        bottom[H-h-1] += bottom[H-h]
    }
    if h-1 >= 0 {
        top[h] += top[h-1]
    }
}

let sumArr = (1...H).map{bottom[$0] + top[$0]}
let minValue = sumArr.min()!
let count = sumArr.filter{$0 == minValue}.count
print(minValue, count)
