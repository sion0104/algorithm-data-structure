import Foundation

func solution(_ n:Int) -> [Int] {
    var answer: [Int] = []
    
    var num = n
    
    while num != 1 {
        answer.append(num)

        
        if num % 2 == 0 {
            num = num / 2
        } else {
            num = 3 * num + 1
        }
    }
    
    answer.append(num)
    
    return answer
}