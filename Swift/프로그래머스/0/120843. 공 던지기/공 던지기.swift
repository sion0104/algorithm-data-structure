import Foundation

func solution(_ numbers:[Int], _ k:Int) -> Int {
    var answer = 0
    let count = numbers.count
    
    for index in 0..<(k-1) {
         answer += 2
        
        if answer >= count {
            answer = answer % count
        }
    }
   
    return numbers[answer]
}