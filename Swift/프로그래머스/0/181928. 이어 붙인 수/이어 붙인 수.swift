import Foundation

func solution(_ num_list:[Int]) -> Int {
    var evenNum = ""
    var oddNum = ""
    
    for num in num_list {
        if num % 2 == 0 {
            evenNum += "\(num)"
        } else {
            oddNum += "\(num)"
        }
    }
    
    let oddNumInt = Int(oddNum) ?? 0
    let evenNumInt = Int(evenNum) ?? 0
    
    return oddNumInt + evenNumInt
}