import Foundation

func solution(_ numbers:[Int], _ direction:String) -> [Int] {
    var rotatedNumbers = numbers
    
    if direction == "right" {
        if let last = rotatedNumbers.popLast() {
            rotatedNumbers.insert(last, at: 0)
        }
    } else if direction == "left" {
        let first = rotatedNumbers.removeFirst()
        rotatedNumbers.append(first)
    }
    return rotatedNumbers
}