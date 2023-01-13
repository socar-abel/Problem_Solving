import Foundation

func solution(_ ingredient:[Int]) -> Int {
    var answer = 0
    var stack = [Int]()
    let standard = [1, 2, 3, 1]
    var i = 0
    
    while i < ingredient.count {
        let now = ingredient[ingredient.index(ingredient.startIndex, offsetBy: i)]
        stack.append(now)
        let tempBurger = Array(stack.suffix(4))
        //print(tempBurger)
        if tempBurger == standard {
            answer += 1
            stack.removeLast(4)
        }
        i += 1
    }
    
    return answer
}
