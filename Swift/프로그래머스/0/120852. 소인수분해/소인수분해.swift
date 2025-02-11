import Foundation

func solution(_ n:Int) -> [Int] {
    var factors = [Int]()
    
    var num = n
    
    var i = 2
    while i * i <= num {
        if num % i == 0 {
            factors.append(i)
            
            while num % i == 0 {
                num = num / i
            }
        } else {
            i += 1
        }
    }
    
    if num > 1 {
        factors.append(num)
    }
    
    return factors
}