import Foundation

func solution(_ my_str:String, _ n:Int) -> [String] {
    var result: [String] = []
    
    let length = my_str.count
    var index = my_str.startIndex
    
    while index < my_str.endIndex {
        let end = my_str.index(index, offsetBy: n, limitedBy: my_str.endIndex) ?? my_str.endIndex
        result.append(String(my_str[index..<end]))
        index = end
    }
    return result
    
}