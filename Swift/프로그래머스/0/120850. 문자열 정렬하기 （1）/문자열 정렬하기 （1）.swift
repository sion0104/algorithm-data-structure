import Foundation

func solution(_ my_string:String) -> [Int] {
    var answer = [Int]()
    for char in my_string{
        if char.isNumber {
            let string = String(char)
            if let num = Int(string) {
                answer.append(num)
            }
        }
    }
    return answer.sorted()
}