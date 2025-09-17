func solution(_ a:Int, _ b:Int) -> String {
    let week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    let month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    let weekIndex = month[0..<a-1].reduce(0, +) + b
    
    return week[(weekIndex - 1) % 7]
}