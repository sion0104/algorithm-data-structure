import Foundation

func solution(_ strlist:[String]) -> [Int] {
    var result = [Int]()
    for word in strlist {
        result.append(word.count)
    }
    return result
}