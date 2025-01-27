import Foundation

func solution(_ arr:[Int], _ idx:Int) -> Int {
    var answer = -1
    
    for i in idx..<arr.count {
        if arr[i] == 1 {
            return i
        }
    }
    return answer
}