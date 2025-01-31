import Foundation

func solution(_ arr:[Int]) -> [Int] {
    var answer: [Int] = []
    for index in 0..<arr.count {
        
        var num = arr[index]
        
        if num >= 50 && num % 2 == 0 {
            num = num / 2
        } else if num < 50 && num % 2 != 0 {
            num = num * 2
        }
        answer.append(num)
    }
    
    return answer
}