import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    var count = my_string.count - n
    
    let startIndex = my_string.index(my_string.startIndex, offsetBy: count)
    let endIndex = my_string.index(my_string.startIndex, offsetBy: count + n - 1)
    
    let subString = my_string[startIndex...endIndex]

    return String(subString)
}