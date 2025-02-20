import Foundation

func solution(_ keyinput:[String], _ board:[Int]) -> [Int] {
    var position = [0, 0]
    
    let maxX = (board[0] - 1) / 2
    let maxY = (board[1] - 1) / 2
    
    let moves: [String: (Int, Int)] = [
        "up": (0, 1),
        "down": (0, -1),
        "left": (-1, 0), 
        "right": (1, 0)
    ]
    
    for key in keyinput {
        if let move = moves[key] {
            let newX = position[0] + move.0
            let newY = position[1] + move.1
            
            if maxX * -1 <= newX && newX <= maxX {
                position[0] = newX
            }
            
            if maxY * -1 <= newY && newY <= maxY {
                position[1] = newY
            }
        }
    }
    return position
}