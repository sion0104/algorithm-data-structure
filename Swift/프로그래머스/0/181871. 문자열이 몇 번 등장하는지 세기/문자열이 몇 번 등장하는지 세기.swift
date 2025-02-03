import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    var answer = 0                
    for index in 0...myString.count-pat.count {
        var startIndex = myString.index(myString.startIndex, offsetBy: index)
        var endIndex = myString.index(startIndex, offsetBy: pat.count)
        
        let subString = String(myString[startIndex..<endIndex]) 
        
        if subString == pat {
            answer += 1
        }
    }
    
    return answer
}