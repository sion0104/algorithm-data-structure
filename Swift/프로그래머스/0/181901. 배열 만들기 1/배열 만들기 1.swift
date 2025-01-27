import Foundation

func solution(_ n:Int, _ k:Int) -> [Int] {
    var result: [Int] = []
    
    for i in 1...Int(n / k) {
        result.append(k * i)
    }
    
    return result
}