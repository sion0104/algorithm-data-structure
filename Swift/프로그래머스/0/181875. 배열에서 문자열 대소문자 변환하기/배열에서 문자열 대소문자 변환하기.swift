import Foundation

func solution(_ strArr:[String]) -> [String] {
    var answer: [String] = []
    
    for index in 0..<strArr.count {
        if index % 2 == 0 {
            answer.append(strArr[index].lowercased())
        } else {
            answer.append(strArr[index].uppercased())
        }
    }
    
    return answer
}