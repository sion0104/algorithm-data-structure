import Foundation

func solution(_ l:Int, _ r:Int) -> [Int] {
    var result = [Int]()
    
     func generateNumbers(_ current: String) {
        if let number = Int(current), number >= l, number <= r {
            result.append(number)
        }
        
        if let number = Int(current), number > r {
            return
        }

        generateNumbers(current + "0")
        generateNumbers(current + "5")
    }
    
    generateNumbers("5")
    
    result.sort()
    
    return result.isEmpty ? [-1] : result
}