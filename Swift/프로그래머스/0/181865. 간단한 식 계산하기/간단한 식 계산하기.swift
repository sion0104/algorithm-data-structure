import Foundation

func solution(_ binomial:String) -> Int {
    let parts = binomial.split(separator: " ").map{ String($0) }
    
    if let a = Int(parts[0]), let b = Int(parts[2]) {
        let operation = parts[1]
        
        switch operation {
            case "+": return a + b 
            case "*": return a * b
            case "-": return a - b
            default: return 0
        }
    }
    return 0
}