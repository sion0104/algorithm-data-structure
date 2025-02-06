import Foundation

func solution(_ arr:[Int], _ flag:[Bool]) -> [Int] {
    var answer = [Int]()
    for index in 0..<flag.count {
        if flag[index] {
            for _ in 0..<arr[index]*2 {
                answer.append(arr[index])
            }
        } else {
            for _ in 0..<arr[index] {
                answer.removeLast()
            }
        }
    }
    
    return answer
}