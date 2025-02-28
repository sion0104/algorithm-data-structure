import Foundation

func solution(_ n: Int) -> Int {
    var result = 0
    var number = 0
    
    for _ in 1...n {
        number += 1
        while (number % 3 == 0 || String(number).contains("3")) {
            number += 1
        }
        result = number
    }
    
    return result
}