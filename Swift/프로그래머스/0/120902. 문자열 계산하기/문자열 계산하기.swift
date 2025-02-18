import Foundation

func solution(_ my_string:String) -> Int {
    let operation_list = my_string.split(separator: " ")
    
    var answer = Int(operation_list[0]) ?? 0
    for index in stride(from: 1, to:operation_list.count, by: 2) {
        let num = Int(operation_list[index + 1]) ?? 0
        
        if operation_list[index] == "+" {
            answer += num
        } else {
           answer -= num 
        }    
    }
    
    return answer
}