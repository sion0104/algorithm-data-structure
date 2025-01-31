import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var answer: [Int] = []
    
    for index in 0..<numbers.count {
        answer.append(numbers[index]  * 2)
    }
    
    return answer
}