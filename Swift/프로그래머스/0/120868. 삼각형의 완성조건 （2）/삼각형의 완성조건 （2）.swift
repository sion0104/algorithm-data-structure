import Foundation

func solution(_ sides:[Int]) -> Int {
    var lengths = [Int]()
    let sortedSides = sides.sorted()
    
    var temp = sortedSides[1] - sortedSides[0]
    
    for i in temp..<sortedSides[1]{
        lengths.append(i)
    }
    
    temp = (sortedSides[1] + sortedSides[0])
    
    for i in (sortedSides[1] + 1)..<temp {
        if !lengths.contains(i) {
            lengths.append(i)
        }
    }
    
    return lengths.count
}