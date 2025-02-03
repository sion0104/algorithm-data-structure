import Foundation

func solution(_ strArr:[String]) -> [String] {
    var answer = [String]()
    for index in 0..<strArr.count {
        let str = strArr[index]
        if !str.contains("ad") {
           answer.append(str)
        }
    }
    return answer
}