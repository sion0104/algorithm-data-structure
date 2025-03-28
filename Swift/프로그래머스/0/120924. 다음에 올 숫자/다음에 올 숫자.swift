import Foundation

func solution(_ common:[Int]) -> Int {
    if common[1] - common[0] == common[2] - common[1] {
        let diff = common[1] - common[0]
        return common.last! + diff
    } else {
        let ratio = common[1] / common[0]
        return common.last! * ratio
    }
    
    return 0
    
}