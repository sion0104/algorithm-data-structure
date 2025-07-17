import Foundation

func solution(_ n:Int) -> Int {
    var answer = 2
    
    while answer <= Int(n/2) {
        if n % answer == 1 {
            return answer
        }
        answer += 1
    }
    
    return n - 1
}