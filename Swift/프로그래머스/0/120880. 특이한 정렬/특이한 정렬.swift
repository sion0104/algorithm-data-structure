import Foundation

func solution(_ numlist:[Int], _ n:Int) -> [Int] {
    return numlist.sorted { (a, b) -> Bool in
        let distA = abs(a - n)
        let distB = abs(b - n)
        
        if distA == distB {
            return a > b
        }
        return distA < distB
    }
}