import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let lenA = String(a).count
    let lenB = String(b).count
    
    let option1 = a * Int(pow(10.0, Double(lenB))) + b
    
    
    return max(option1, 2*a*b)
}