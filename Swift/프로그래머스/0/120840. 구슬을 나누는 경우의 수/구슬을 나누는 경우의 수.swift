import Foundation

func factorial(_ n: Int) -> Decimal {
    return (1...n).reduce(Decimal(1)) { result, value in
        result * Decimal(value)
    }
}

func combination(_ n: Int, _ k: Int) -> Decimal {
    if k == 0 || k == n {
        return 1
    }
    
    let numerator = factorial(n)
    let denominator = factorial(n - k) * factorial(k)
    
    return numerator / denominator
}

func solution(_ balls: Int, _ share: Int) -> Int {
    return NSDecimalNumber(decimal: combination(balls, share)).intValue
}