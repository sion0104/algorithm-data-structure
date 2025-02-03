import Foundation

func solution(_ dartResult:String) -> Int {
    var scores = [Int]()
    var currentScore = ""
    
    for char in dartResult {
        if char.isNumber {
            currentScore += String(char)
        } else {
            if let scoreNumber = Int(currentScore) {
                scores.append(scoreNumber)
                currentScore = ""
            }
            
            if char == "S" {
                scores[scores.count-1] = Int(pow(Double(scores.last!), 1.0))
            } else if char == "D" {
                scores[scores.count-1] = Int(pow(Double(scores.last!), 2.0))
            } else if char == "T" {
                scores[scores.count-1] = Int(pow(Double(scores.last!), 3.0))
            } else if char == "*" {
                if scores.count > 1 {
                    scores[scores.count - 2] *= 2
                }
                scores[scores.count - 1] *= 2
            } else if char == "#" {
                scores[scores.count - 1] *= -1
            }
        }
    }
    
    return scores.reduce(0, +)
}