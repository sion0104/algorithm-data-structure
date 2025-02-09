import Foundation

func solution(_ n:Int) -> [[Int]] {
    var matrix = Array(repeating: Array(repeating: 0, count: n), count: n)
    let directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    var directionIndex = 0
    
    var row = 0
    var col = 0
    for num in 1...(n*n) {
        matrix[row][col] = num
        
        var nextRow = row + directions[directionIndex].0
        var nextCol = col + directions[directionIndex].1
        
        if !(0..<n).contains(nextRow) || !(0..<n).contains(nextCol) || matrix[nextRow][nextCol] != 0 {
            directionIndex = (directionIndex + 1) % 4
            
            nextRow = row + directions[directionIndex].0
            nextCol = col + directions[directionIndex].1
        }
        
        row = nextRow
        col = nextCol
    }
    
    return matrix
}