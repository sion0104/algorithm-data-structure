import Foundation

func solution(_ myString:String, _ pat:String) -> String {
    for length in (pat.count...myString.count).reversed() {
        let endIndex = myString.index(myString.startIndex, offsetBy: length)
        let subString = String(myString[myString.startIndex..<endIndex])
        
        if subString.hasSuffix(pat) {
            return subString
        }
    }
    
    return ""
}