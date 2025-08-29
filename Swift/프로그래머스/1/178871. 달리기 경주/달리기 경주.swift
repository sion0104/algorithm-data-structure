import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
     var players = players
    
    var answer: [String: Int] = [:]
    for (i, player) in players.enumerated() {
        answer[player] = i
    }
    
    for name in callings {
        if let index = answer[name], index > 0 {
            players.swapAt(index, index - 1)
            
            answer[name] = index - 1
            
            let frontPlayer = players[index] 
            answer[frontPlayer] = index
        }
    }
    
    return players
}