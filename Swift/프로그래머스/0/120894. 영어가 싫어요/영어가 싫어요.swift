import Foundation

func solution(_ numbers:String) -> Int64 {
    let numberDict = [
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    ]
    
    var resultString = numbers
    for (word, digit) in numberDict {
        resultString = resultString.replacingOccurrences(of: word, with: digit)
    }
        
    return Int64(resultString) ?? 0
}