import Foundation

func solution(_ emergency:[Int]) -> [Int] {
    let sortedEmergency = emergency.enumerated().sorted { $0.element > $1.element }  
    
    var result = [Int](repeating: 0, count: emergency.count)
    
    for (order, (index, _)) in sortedEmergency.enumerated() {
        result[index] = order + 1
    }
    
    return result
}