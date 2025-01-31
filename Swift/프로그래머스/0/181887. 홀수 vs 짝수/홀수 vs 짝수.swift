import Foundation

func solution(_ num_list:[Int]) -> Int {
    var odd_num = 0
    var even_num = 0
    
    for index in 0..<num_list.count {
        if index % 2 == 0 {
            odd_num += num_list[index]
        } else {
            even_num += num_list[index]
        }
    }
    return max(odd_num, even_num)
}