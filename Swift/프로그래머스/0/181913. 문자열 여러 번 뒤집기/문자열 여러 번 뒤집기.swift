import Foundation

func solution(_ my_string:String, _ queries:[[Int]]) -> String {
    var chars = Array(my_string)
    
    for query in queries {
        let s = query[0]
        let e = query[1]
        
        chars[s...e].reverse()
    }
    return String(chars)
}