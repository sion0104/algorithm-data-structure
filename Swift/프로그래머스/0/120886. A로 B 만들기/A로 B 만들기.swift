import Foundation

func solution(_ before:String, _ after:String) -> Int {
    var beforeDict: [Character: Int] = [:]
    var afterDict: [Character: Int] = [:]
    
    for char in before {
        beforeDict[char, default: 0] += 1
    }
    
    for char in after {
        afterDict[char, default: 0] += 1
    }
    
    return beforeDict == afterDict ? 1 : 0
}