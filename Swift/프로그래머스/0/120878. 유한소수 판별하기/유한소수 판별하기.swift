import Foundation

func gcd(_ a: Int, _ b: Int) -> Int {
    if b == 0 {
        return a
    } else {
        return gcd(b, a % b)
    }
}

func solution(_ a:Int, _ b:Int) -> Int {
    var b_remainder = b / gcd(a, b)
    
    while b_remainder % 2 == 0 {
        b_remainder = b_remainder / 2
    }
    
    while b_remainder % 5 == 0 {
        b_remainder = b_remainder / 5
    }
    
    if b_remainder == 1 {
        return 1
    }
    return 2
}