import Foundation

func solution(_ my_string:String) -> String {
    var answer = [String]()
    
    for char in my_string {
        if !answer.contains(String(char)) {
            answer.append(String(char))
        }
    }
    
    return answer.joined(separator: "")
}