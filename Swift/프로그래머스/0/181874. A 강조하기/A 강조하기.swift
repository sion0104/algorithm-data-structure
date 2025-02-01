import Foundation

func solution(_ myString:String) -> String {
    var answer: String = ""
    
    for char in myString {
        if char == "a" {
            answer += char.uppercased()
        } else if char == "A" {
            answer += "A"
        } else {
            answer += char.lowercased()
        }
    }
    
    return answer
}