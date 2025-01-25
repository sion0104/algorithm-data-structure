import Foundation

func solution(_ my_string:String) -> [String] {
    var answer: [String] = []
    
    for i in 0..<my_string.count {
        
        let startIndex = my_string.index(my_string.startIndex, offsetBy: i)
        let endIndex = my_string.index(startIndex, offsetBy: my_string.count - i - 1)
        let subString = my_string[startIndex...endIndex]

        answer.append(String(subString))
    }
    
    answer.sort()
    
    return answer
}