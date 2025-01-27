import Foundation

func solution(_ my_string:String, _ indices:[Int]) -> String {
    var myStringArray = Array(my_string)
    
    for indice in indices {
        myStringArray[indice] = "0"
    }
    
    while myStringArray.contains("0") {
        if let firstIndex = myStringArray.firstIndex(of: "0") {
            myStringArray.remove(at: firstIndex)
        }
    }
    
    return String(myStringArray)
}