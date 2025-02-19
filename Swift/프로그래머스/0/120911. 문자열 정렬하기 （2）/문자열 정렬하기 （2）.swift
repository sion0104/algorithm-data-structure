import Foundation

func solution(_ my_string:String) -> String {
    var answer = Array(my_string.lowercased())
    answer.sort()
    
    return String(answer)
}