import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var count = 0
    var answer: [Int]
    
    for win_num in win_nums{
        if lottos.contains(win_num) {
            count += 1
        }
    }
    
    let zeroCount = lottos.filter { $0 == 0 }.count 
    
    let maxRank = min(6, 7 - (count + zeroCount))
    
    let minRank = min(6, 7 - count)
    
    answer = [maxRank, minRank]
    
    return answer
}