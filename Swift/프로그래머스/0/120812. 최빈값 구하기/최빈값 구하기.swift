import Foundation

func solution(_ array:[Int]) -> Int {
    var countDict: [Int: Int] = [:]
    
    for num in array {
        countDict[num, default: 0] += 1
    }
    
    let maxCount = countDict.values.max() ?? -1

    let maxCountOccurrences = countDict.values.filter { $0 == maxCount }.count

    if maxCountOccurrences > 1 {
        return -1
    }
    
    for (key, value) in countDict {
        if value == maxCount {
            return key
        }
    }
    
    return -1
}