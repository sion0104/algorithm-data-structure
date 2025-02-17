import Foundation

func solution(_ my_string:String) -> String {
    var answer = ""
    for char in my_string{
        if char.isUppercase {
            answer += char.lowercased()
        } else {
            answer += char.uppercased()
        }
    }
    return answer
}