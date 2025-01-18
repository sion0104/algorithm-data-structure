import Foundation

func solution(_ n:Int) -> Int {
    var answer: Int = 0
    
    if n % 2 == 0 {
        for i in stride(from: 2, through: n, by: 2) {
            answer += Int(pow(Double(i), 2))
        }
    } else {
        for i in stride(from: 1, through: n, by: 2) {
            answer += i
        }
    }
    return answer
}