import Foundation

func solution(_ my_string:String, _ m:Int, _ c:Int) -> String {
    if m == 1 {
        return my_string
    }
    
    var i = c - 1
    var answer = ""
    
    while i < my_string.count {
        let index = my_string.index(my_string.startIndex, offsetBy: i)
        
        answer += String(my_string[index])
        
        i += m
    }
    
    return answer
}