import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    let transformed = myString.map{ (char) -> Character in
        switch char {
            case "A": return "B"
            case "B": return "A"
            default : return char
        }
    }
    
    let transformedString = String(transformed)
    
    if transformedString.contains(pat) {
        return 1
    } else {
        return 0
    }
    
    return 0
}