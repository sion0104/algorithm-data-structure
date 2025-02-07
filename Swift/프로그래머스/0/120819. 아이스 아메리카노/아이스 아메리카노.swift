import Foundation

func solution(_ money:Int) -> [Int] {
    let answer = [Int(money / 5500), money % 5500]
    
    return answer
}