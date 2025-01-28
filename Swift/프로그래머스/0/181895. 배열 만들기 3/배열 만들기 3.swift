import Foundation

func solution(_ arr:[Int], _ intervals:[[Int]]) -> [Int] {
    var answer: [Int] = []
    
    for interval in intervals {
        var a = interval[0]
        var b = interval[1]
        
        answer += arr[a...b]
    }
    return answer
}