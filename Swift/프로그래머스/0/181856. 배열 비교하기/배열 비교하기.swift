import Foundation

func solution(_ arr1:[Int], _ arr2:[Int]) -> Int {
    var arr1Score = arr1.count
    var arr2Score = arr2.count
    
    while true {
        if arr1Score > arr2Score {
            return 1
        } else if arr1Score < arr2Score {
            return -1
        } else {
            arr1Score = arr1.reduce(0, +)
            arr2Score = arr2.reduce(0, +)
        }

        if arr1Score == arr2Score {
            return 0
        }
    }
}