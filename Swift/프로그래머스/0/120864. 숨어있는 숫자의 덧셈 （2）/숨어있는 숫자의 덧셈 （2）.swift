import Foundation

func solution(_ my_string:String) -> Int {
    var sum = 0
    var currentNumber = ""
    
    for char in my_string {
        if char.isNumber {
            currentNumber.append(char)
        } else {
            if !currentNumber.isEmpty {
                sum += Int(currentNumber)!
                currentNumber = ""
            }
        }
    }
    
    if !currentNumber.isEmpty {
        sum += Int(currentNumber)!
    }
    
    return sum
}