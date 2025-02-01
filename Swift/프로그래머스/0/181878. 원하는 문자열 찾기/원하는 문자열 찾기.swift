import Foundation

func solution(_ myString:String, _ pat:String) -> Int {
    if myString.lowercased().contains(pat.lowercased()) {
        return 1
    } else {
        return 0
    }
}