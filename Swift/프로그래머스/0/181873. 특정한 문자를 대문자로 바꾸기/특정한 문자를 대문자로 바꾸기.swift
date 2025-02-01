import Foundation

func solution(_ my_string:String, _ alp:String) -> String {
    var answer: String = ""
    
    for char in my_string {
        var string = String(char)
        if string == alp {
            answer += string.uppercased()
        } else {
            answer += string
        }
    }
    
    return answer
}