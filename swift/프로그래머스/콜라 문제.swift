import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var answer = 0
    var tempCola = n
    
    while tempCola >= a {
        let changedCola = Int(tempCola/a) * b
        let remainedCola = tempCola % a
        
        answer += changedCola
        tempCola = changedCola + remainedCola
    }
    
    return answer
}
