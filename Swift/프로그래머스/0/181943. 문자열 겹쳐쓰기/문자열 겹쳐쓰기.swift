import Foundation

func solution(_ my_string:String, _ overwrite_string:String, _ s:Int) -> String {
    let startIndex = my_string.index(my_string.startIndex, offsetBy: s)
    let endIndex = my_string.index(startIndex, offsetBy: overwrite_string.count)
    
    let replaced = String(my_string[..<startIndex]) + String(overwrite_string) + String(my_string[endIndex...])
    
    return replaced
}