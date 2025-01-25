import Foundation

func solution(_ my_strings:[String], _ parts:[[Int]]) -> String {
    var answer = ""
    for i in 0..<my_strings.count {
        let startIndex = parts[i][0]
        let endIndex = parts[i][1]
        
        let start = my_strings[i].index(my_strings[i].startIndex, offsetBy: startIndex)
        let end = my_strings[i].index(my_strings[i].startIndex, offsetBy: endIndex)
        
        let subString = my_strings[i][start...end]
        answer += String(subString)

    }
    return answer
}