import Foundation

func solution(_ num_list:[Int], _ n:Int) -> [Int] {
    var answer: [Int] = []
    
    var index = 0
    while index < num_list.count {
        answer.append(num_list[index])
        index += n
    }
    
    return answer
}