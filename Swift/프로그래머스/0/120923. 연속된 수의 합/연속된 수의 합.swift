import Foundation

func solution(_ num:Int, _ total:Int) -> [Int] {
    var answer: [Int] = []
    
    let startNum = Int(total / num)
    var middleIndex = 0
    
    if num % 2 == 0 {
        middleIndex = Int(num / 2) - 1
    } else {
        middleIndex = Int(num / 2)
    }
    
    for i in 0..<num {
        answer.append(startNum - middleIndex + i)
    }
    
    return answer
}