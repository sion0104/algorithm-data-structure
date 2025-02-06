import Foundation

func solution(_ arr:[Int], _ k:Int) -> [Int] {
    var result = [Int]()
    
    for i in 0..<arr.count {
        if result.count == k {
            break
        }
        
        if !result.contains(arr[i]) {
            result.append(arr[i])
        }
    }
    
    for _ in 0..<k-result.count {
        result.append(-1)
    }
    
    return result
}