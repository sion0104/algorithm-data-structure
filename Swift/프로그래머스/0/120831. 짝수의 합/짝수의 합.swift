import Foundation

func solution(_ n:Int) -> Int {
    var answer = 0
    
    for i in stride(from: 0, to: n+1, by: 2) {
        answer += i
    }
    
    return answer
}