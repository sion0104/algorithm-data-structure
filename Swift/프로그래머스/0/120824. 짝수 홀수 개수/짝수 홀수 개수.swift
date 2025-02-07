import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var result: [Int] = [0, 0]
    
    for num in num_list {
        var index = num % 2 == 0 ? 0 : 1
        result[index] += 1
    }
    
    return result
}