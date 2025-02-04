import Foundation

func solution(_ myString:String) -> [String] {
    var parts = myString.split(separator: "x").map{ String($0) }
    
    return parts.sorted()
}