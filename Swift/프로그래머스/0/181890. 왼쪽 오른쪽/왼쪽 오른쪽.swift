import Foundation

func solution(_ str_list:[String]) -> [String] {
    var answer: [String] = []
    
    for index in 0..<str_list.count {
        if str_list[index] == "l" {
            answer = Array(str_list[0..<index])
            break
        } else if str_list[index] == "r" {
            answer = Array(str_list[(index+1)..<str_list.count])
            break
        }
    }
    
    return answer
}