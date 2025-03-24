import Foundation

func solution(_ i:Int, _ j:Int, _ k:Int) -> Int {
    var count = 0
    
    for num in i...j {
        let numToString = String(num)
                                 
        if numToString.contains("\(k)") {
            count += numToString.filter({ String($0) == "\(k)" }).count
        }
    }
    
    return count
}