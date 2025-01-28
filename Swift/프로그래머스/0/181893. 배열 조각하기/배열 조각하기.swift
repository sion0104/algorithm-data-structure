import Foundation

func solution(_ arr:[Int], _ query:[Int]) -> [Int] {
    var arr = arr
    
    for (index, value) in query.enumerated() {
        if index % 2 == 0 {
            arr = Array(arr[...value])
        } else {
            arr = Array(arr[value...])
        }
    }
    return arr
}