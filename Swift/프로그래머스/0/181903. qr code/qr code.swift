import Foundation

func solution(_ q:Int, _ r:Int, _ code:String) -> String {
    guard q > 1 else {
        return code
    }
    
    let characters = Array(code)
    let startIndex = r
    var answer = ""
    
    stride(from: startIndex, to: characters.count, by: q).forEach {
        answer.append(characters[$0])
    }
    
    return answer
}