import Foundation

func solution(_ date1:[Int], _ date2:[Int]) -> Int {
    for index in 0..<date1.count {
        if date1[index] < date2[index] {
            return 1
        } else if date1[index] > date2[index] {
            return 0
        }
    }
    return 0
}