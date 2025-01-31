import Foundation

func solution(_ num_list:[Int]) -> Int {
    var result = 0
    
    for num in num_list {
        var temp = num
        
        while temp != 1 {
            if (temp & 1) == 0 {
                temp >>= 1
            } else {
                temp = (temp - 1) >> 1
            }
            result += 1
        }
    }
    return result
}