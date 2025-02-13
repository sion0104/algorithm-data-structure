import Foundation

func solution(_ order:Int) -> Int {
    let num369 = "369"
    
    var answer = 0
    var numStr = String(order)
    
    for char in numStr {
        if num369.contains(char) {
            answer += 1
        }
    }
    
    return answer
}