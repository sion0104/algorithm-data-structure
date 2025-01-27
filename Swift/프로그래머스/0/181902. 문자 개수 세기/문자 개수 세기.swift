import Foundation

func solution(_ my_string:String) -> [Int] {
    var answer = [Int](repeating: 0, count: 52)
    
    for i in my_string.unicodeScalars {
        var unicode = Int(i.value)
        
        if unicode >= 65 && unicode <= 90 {
            answer[unicode - 65] += 1
        } else {
            answer[unicode - 71] += 1
        }
    }

    return answer
}