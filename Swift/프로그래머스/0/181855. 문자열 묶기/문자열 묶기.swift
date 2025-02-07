import Foundation

func solution(_ strArr:[String]) -> Int {
    var numCount = [Int: Int]()
    
    for str in strArr {
        var length = str.count
        
        if let count = numCount[length] {
            numCount[length] = count + 1
        } else {
            numCount[length] = 1
        }
    }
    
    return numCount.values.max() ?? 0
}