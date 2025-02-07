import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    var answer: String = ""
    
    for char in my_string {
        answer += String(repeating: char, count: n)
    }
    
    return answer
}