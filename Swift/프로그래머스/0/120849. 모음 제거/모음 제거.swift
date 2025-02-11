import Foundation

func solution(_ my_string:String) -> String {
    let vowel = "aeiou"
    var answer = ""
    
    for char in my_string {
        if !vowel.contains(char) {
            answer.append(char)
        }
    }
    return answer
}