import Foundation

func solution(_ s:String) -> String {
    var answer = ""
    for char in s {
        if s.filter({ $0 == char }).count == 1 {
            answer.append(char)
        }
    }
    
    return String(answer.sorted())
}