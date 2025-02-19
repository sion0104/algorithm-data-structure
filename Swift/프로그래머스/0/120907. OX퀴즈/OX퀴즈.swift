import Foundation

func solution(_ quiz:[String]) -> [String] {
    var answer = [String]()
    
    for operation in quiz {
        let operationArray = operation.split(separator: " ")
        
        let num1 = Int(operationArray[0]) ?? 0
        let operation = String(operationArray[1])
        let num2 = Int(operationArray[2]) ?? 0
        let NumAnswer = Int(String(operationArray[4])) ?? 0
        
        var guess = 0
        if operation == "+" {
            guess = num1 + num2
        } else {
            guess = num1 - num2
        }
        
        if guess == NumAnswer {
            answer.append("O")
        } else {
            answer.append("X")
        }
    }
    return answer
}