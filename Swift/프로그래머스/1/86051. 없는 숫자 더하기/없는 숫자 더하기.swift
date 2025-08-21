import Foundation

func solution(_ numbers:[Int]) -> Int {
    let zeroToNine : Set<Int> = Set(0...9)
    
    let inputSet = Set(numbers)
    
    let difference = zeroToNine.subtracting(inputSet)
    
    return difference.reduce(0, +)
}