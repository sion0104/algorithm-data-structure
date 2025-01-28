import Foundation

func solution(_ num_list:[Int]) -> Int {
    for index in 0..<num_list.count {
        if num_list[index] < 0 {
            return index
        }
    }
    return -1
}