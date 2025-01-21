import Foundation

func solution(_ a:Int, _ b:Int, _ c:Int) -> Int {
    var result = a + b + c
    
    if a == b || b == c || a == c {
        result *= Int(pow(Double(a), 2.0) + pow(Double(b), 2.0) + pow(Double(c), 2.0))
    }
    
    if a == b && b == c {
        result *= Int(pow(Double(a), 3.0) + pow(Double(b), 3.0) + pow(Double(c), 3.0))
    }
    
    return result
   
}