import Foundation

func solution(_ myString:String) -> [Int] {
    let parts = myString.split(separator: "x", omittingEmptySubsequences: false)
    
    let lengths = parts.map{ $0.count }
    
    return lengths
}