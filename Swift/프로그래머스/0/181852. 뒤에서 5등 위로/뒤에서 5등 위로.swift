import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    var answer = num_list.sorted()
    
    return Array(answer[5..<num_list.count])
}