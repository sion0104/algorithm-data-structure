import Foundation

func solution(_ babbling:[String]) -> Int {
    let possible = ["aya", "ye", "woo", "ma"]
    
    return babbling.filter { word in
        var temp = word
                            
        for sound in possible {
            temp = temp.replacingOccurrences(of: sound, with: " ")
        }
                            
        return temp.trimmingCharacters(in: .whitespaces).isEmpty
    }.count
}