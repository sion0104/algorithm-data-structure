import Foundation

func solution(_ a:Int, _ b:Int) -> Int {
    let lenA = String(a).count
    let lenB = String(b).count
    
    let option1 = a * Int(pow(10.0, Double(lenB))) + b
    let option2 = a + b * Int(pow(10.0, Double(lenA)))
    
    if option1 > option2 {
        return option1
    } else {
        return option2
    }
}