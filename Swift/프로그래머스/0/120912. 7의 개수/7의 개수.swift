import Foundation

func solution(_ array:[Int]) -> Int {
    var answer = 0
    for num in array {
        let strNum = String(num)
        
        answer += strNum.filter{ $0 == "7" }.count
    }
    return answer
}