import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var result = num_list
    let lastIndex = num_list.count - 1
    let frontLastIndex = lastIndex - 1
    
    var num = 0
    if num_list[lastIndex] > num_list[frontLastIndex]{
        num = num_list[lastIndex] - num_list[frontLastIndex]
    } else {
        num = num_list[lastIndex] * 2
    }
    
    result.append(num)
    
    return result
}