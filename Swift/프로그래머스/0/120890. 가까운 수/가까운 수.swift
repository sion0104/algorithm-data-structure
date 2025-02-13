import Foundation

func solution(_ array:[Int], _ n:Int) -> Int {
    var result = array[0]
    
    for num in array {
        if abs(n - result) == abs(n - num) {
            result = min(result, num)
        }
        result = abs(n - result) > abs(n - num) ? num : result
    }
    return result
}