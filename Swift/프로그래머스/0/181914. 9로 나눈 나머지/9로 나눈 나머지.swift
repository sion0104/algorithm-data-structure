import Foundation

func solution(_ number:String) -> Int {
    var answer = 0
    var numArray = Array(number)
    
    for char in numArray {
        if let digit = Int(String(char)) {
            answer += digit
        }
    }
    return answer % 9
}