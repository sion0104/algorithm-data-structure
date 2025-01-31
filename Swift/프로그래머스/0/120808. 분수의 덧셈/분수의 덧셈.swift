import Foundation

func solution(_ numer1:Int, _ denom1:Int, _ numer2:Int, _ denom2:Int) -> [Int] {
    let commonDenom = denom1 * denom2
    let numeratorSum = numer1 * denom2 + numer2 * denom1
    
    let divisor = gcd(numeratorSum, commonDenom)
    
    return [numeratorSum / divisor, commonDenom / divisor]
}

func gcd(_ a: Int, _ b: Int) -> Int {
    let remainder = a % b
    if remainder != 0 {
        return gcd(b, remainder)
    } else {
        return b
    }
}