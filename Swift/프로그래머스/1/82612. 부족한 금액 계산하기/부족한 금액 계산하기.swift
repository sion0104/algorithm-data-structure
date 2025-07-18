import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    var sum: Int64 = 0
    
    for i in 1...count {
        sum += Int64(i)
    }
    
    if Int64(money) > Int64(price) * sum {
        return 0
    }
    
    return Int64(price) * sum - Int64(money)
}