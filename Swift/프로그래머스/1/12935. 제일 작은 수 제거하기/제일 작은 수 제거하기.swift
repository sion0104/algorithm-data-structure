func solution(_ arr:[Int]) -> [Int] {
    var answer = arr
    
    if arr.count == 1 {
        return [-1]
    }
    
    let minNum = arr.min()!
    
    if let index = answer.firstIndex(of: minNum) {
        answer.remove(at: index)
    }
    
    return answer
}