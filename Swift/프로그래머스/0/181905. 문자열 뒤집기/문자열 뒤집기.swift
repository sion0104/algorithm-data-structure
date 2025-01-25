import Foundation

func solution(_ my_string:String, _ s:Int, _ e:Int) -> String {
    var myStringArray = Array(my_string)
    
    let startIndex = my_string.index(my_string.startIndex, offsetBy: s)
    let endIndex = my_string.index(my_string.startIndex, offsetBy: e)
    
    let reversedSubString = String(my_string[startIndex...endIndex]).reversed()
    
    myStringArray.replaceSubrange(s...e, with: reversedSubString)
    
    return String(myStringArray)
}