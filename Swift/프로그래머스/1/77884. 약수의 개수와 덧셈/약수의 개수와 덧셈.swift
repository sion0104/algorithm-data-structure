import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var result = 0 
    for i in left...right {
        let count = numberOfDivisors(i)
        
        if count % 2 == 0 {
            result += i
        } else {
            result -= i
        }
    }
    
    return result
}

func numberOfDivisors(_ n: Int) -> Int {
    if n <= 0 {
        return 0
    }
    
    var num = n
    var divisorCount = 1
    var i = 2
    
    while i * i <= num {
        var count = 0
        while num % i == 0 {
            count += 1
            num /= i
        }
        divisorCount *= (count + 1)
        i += 1
    }
    
    if num > 1 {
        divisorCount *= 2
    }
    
    return divisorCount
}
