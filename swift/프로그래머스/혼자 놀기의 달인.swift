import Foundation

func solution(_ cards:[Int]) -> Int {
    var answer = 0
    
    for i in 1...cards.count {
        answer = max(answer, getGameResult(cards: cards, firstSelectedBox: i))
    }
    
    return answer
}


func getGameResult(cards:[Int], firstSelectedBox:Int) -> Int {
    var result = 0
    let num = cards.count
    var boxGroupOne = Set<Int>()
    var boxGroupTwo = Set<Int>()
    var selectedBox = firstSelectedBox
    var nextSelectedBox = -1

    while true {
        boxGroupOne.insert(selectedBox)
        nextSelectedBox = cards[selectedBox-1]
        if boxGroupOne.contains(nextSelectedBox) {
            break
        }
        selectedBox = nextSelectedBox
    }
    
    if boxGroupOne.count == cards.count {
        return 0
    }
    
    for i in 1...num {
        if boxGroupOne.contains(i) {
            continue
        }
        selectedBox = i
        while true {
            boxGroupTwo.insert(selectedBox)
            nextSelectedBox = cards[selectedBox-1]
            if boxGroupOne.contains(nextSelectedBox) || boxGroupTwo.contains(nextSelectedBox) {
                break
            }
            selectedBox = nextSelectedBox
        }
        
        result = max(result, boxGroupOne.count * boxGroupTwo.count)
        boxGroupTwo = Set<Int>()
    }
    
    return result
}
