import Foundation

func solution(_ my_string:String) -> [String] {
    var answer: [String] = []
    
    for i in 0..<my_string.count {
        
        let startIndex = my_string.index(my_string.startIndex, offsetBy: i)
        let subString = my_string[startIndex...]

        answer.append(String(subString))
    }
    
    answer.sort()
    
    return answer
}