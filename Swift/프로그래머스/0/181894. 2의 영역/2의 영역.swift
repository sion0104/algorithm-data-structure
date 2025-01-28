import Foundation

func solution(_ arr:[Int]) -> [Int] {
    if let startIndex = arr.firstIndex(of: 2), let endIndex = arr.lastIndex(of : 2) {
        return Array(arr[startIndex...endIndex])
    } else {
        return [-1]
    }
}