import Foundation

func solution(_ num_list:[Int], _ n:Int) -> Int {
    for i in num_list {
        if i == n {
            return 1
        }
    }
    return 0
}