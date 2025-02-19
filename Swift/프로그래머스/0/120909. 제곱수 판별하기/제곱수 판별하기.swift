import Foundation

func solution(_ n:Int) -> Int {
    if pow(Double(Int(sqrt(Double(n)))), 2.0) == Double(n) {
        return 1
    } 
    return 2
}