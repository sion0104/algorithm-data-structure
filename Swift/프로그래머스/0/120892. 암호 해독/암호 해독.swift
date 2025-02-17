import Foundation

func solution(_ cipher:String, _ code:Int) -> String {
    var answer = [String]()
    
    for index in stride(from: code - 1, through: cipher.count-1, by: code) {
        let numIndex = cipher.index(cipher.startIndex, offsetBy: index)
        answer.append(String(cipher[numIndex]))
    }
    
    return answer.joined(separator: "")
}