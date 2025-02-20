import Foundation

func solution(_ numbers:[Int]) -> Int {
    let sortedNumbers = numbers.sorted()
    
    let maxProduct1 = sortedNumbers[sortedNumbers.count - 1] * sortedNumbers[sortedNumbers.count - 2]
    let maxProduct2 = sortedNumbers[0] * sortedNumbers[1]
    
    return max(maxProduct1, maxProduct2)
}