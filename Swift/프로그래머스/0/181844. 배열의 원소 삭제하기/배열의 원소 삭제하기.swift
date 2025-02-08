import Foundation

func solution(_ arr:[Int], _ delete_list:[Int]) -> [Int] {
    var result = arr
    
    for delete in delete_list {
        if let deleteIndex = result.firstIndex(of: delete) {
            result.remove(at: deleteIndex)
        }
    }
    
    return result
}