import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var playing = [Int: Int]()
    var failure = [(Int, Float)]()
    var total = stages.count
    
    for stage in stages {
        playing[stage, default: 0] += 1
    }
    
    for x in 1...N {
        let reached = total - playing[x-1, default: 0]
        total -= playing[x-1, default: 0]
        if reached == 0 {
            failure.append((x, 0.0))
        }
        else {
            failure.append((x, Float(playing[x, default: 0])/Float(reached)))
        }
    }
    
    failure.sort{$0.0 < $1.0}
    failure.sort{$0.1 > $1.1}
                           
    return failure.map{$0.0}
}
