import Foundation

func solution(_ data:[[Int]], _ col:Int, _ row_begin:Int, _ row_end:Int) -> Int {
    var answer = -1
    let data = data.sorted { $0[col-1] == $1[col-1] ? $0[0] > $1[0] : $0[col-1] < $1[col-1] }

    for i in row_begin...row_end {
        let tempS = data[i-1].reduce(0) { $0 + ($1 % i) }
        answer = answer == -1 ? tempS : answer ^ tempS
    }

    return answer
}
