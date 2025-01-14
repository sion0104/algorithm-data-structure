import Foundation

func solution(_ record:[String]) -> [String] {
    var messageLog: [(String, String)] = []
    var userInfo: [String : String] = [:]
    
    for entry in record {
        let parts = entry.split(separator: " ").map{ String($0) }
        let action = parts[0]
        let userId = parts[1]
        
        if action == "Enter" {
            let nickname = parts[2]
            userInfo[userId] = nickname
            messageLog.append((userId, "님이 들어왔습니다."))
        } else if action == "Leave"{
            messageLog.append((userId, "님이 나갔습니다."))
        } else if action == "Change" {
            let nickname = parts[2]
            userInfo[userId] = nickname
        }
    }
    
    var finalMessages: [String] = []
    
    for log in messageLog {
        let userId = log.0
        let message = log.1
        if let nickname = userInfo[userId] {
            finalMessages.append("\(nickname)\(message)")
        }
    }
    
    return finalMessages
}
