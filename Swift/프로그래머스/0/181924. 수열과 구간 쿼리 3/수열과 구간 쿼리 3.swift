import Foundation

func solution(_ arr:[Int], _ queries:[[Int]]) -> [Int] {
    var result = arr
    
    for query in queries {
        var i = query[0]
        var j = query[1]
        
        let temp = result[i]
        result[i] = result[j]
        result[j] = temp
    }
    
    return result
}