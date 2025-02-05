import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer = [Int]()
    
    for num in arr {
        for i in 0..<num {
            answer.append(num)
        }
    }
    
    return answer
}