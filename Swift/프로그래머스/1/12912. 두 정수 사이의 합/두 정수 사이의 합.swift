func solution(_ a:Int, _ b:Int) -> Int64 {
    var answer = 0
    
    for i in a<b ? a...b : b...a {
        answer += i
    }
    
    return Int64(answer)
}