import Foundation

func solution(_ arr:[[Int]]) -> [[Int]] {
    var matrix = arr
    
    let rows = arr.count
    let cols = arr[0].count
    
    if rows > cols {
        for i in 0..<rows {
            matrix[i] += Array(repeating: 0, count: rows - cols)
        }
    } else if cols > rows {
        let extraRows = Array(repeating: Array(repeating: 0, count: cols), count: cols - rows)
        matrix.append(contentsOf: extraRows)
    }
    return matrix 
}