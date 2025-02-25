import Foundation

func solution(_ board:[[Int]]) -> Int {
    let n = board.count
    var dangerZones = Array(repeating: Array(repeating: 0, count: n), count: n)
    let directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in 0..<n {
        for j in 0..<n {
            if board[i][j] == 1 {
                dangerZones[i][j] = 1
                for direction in directions {
                    let ni = i + direction.0
                    let nj = j + direction.1
                    if ni >= 0 && ni < n && nj >= 0 && nj < n {
                        dangerZones[ni][nj] = 1
                    }
                }
            }
        }
    }

    var safeCount = 0

    for i in 0..<n {
        for j in 0..<n {
            if dangerZones[i][j] == 0 && board[i][j] == 0 {
                safeCount += 1
            }
        }
    }

    return safeCount
}