import Foundation

func solution(_ num_list: [Int]) -> [Int] {
    var result = num_list

    if let last = num_list.last, let secondLast = num_list.dropLast().last {
        let num = last > secondLast ? last - secondLast : last * 2
        result.append(num)
    }
    
    return result
}