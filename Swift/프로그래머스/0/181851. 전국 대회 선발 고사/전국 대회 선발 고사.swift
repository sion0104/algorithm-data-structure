import Foundation

func solution(_ rank:[Int], _ attendance:[Bool]) -> Int {
    var array = [(Int, Int)]()
    
    for (index, isPresent) in attendance.enumerated() {
        if isPresent {
            array.append((rank[index], index))
        }
    }
    
    array.sort{ $0.0 < $1.0 }
    
    return 10000 * array[0].1 + 100 * array[1].1 + array[2].1
}