import Foundation

func solution(_ n:Int) -> [[Int]] {
    var answer = [[Int]]()
    
    for i in 0..<n {
        var line = Array(repeating: 0, count: n)
        
        line[i] = 1
        
        answer.append(line)
    }
    
    return answer
}