import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    var numA = a % 2
    var numB = b % 2
    if numA + numB == 2 {
        return Int(pow(Double(a), 2.0) + pow(Double(b), 2.0))
    } else if numA + numB == 1 {
        return 2 * (a + b)
    } else {
        return abs(a - b)
    }
    return 0
}