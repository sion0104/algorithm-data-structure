func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    var answer: [String] = Array(repeating: "", count: n)
    
    for i in 0..<n {
        var binary: String = String(arr1[i] | arr2[i], radix: 2)
        
        while binary.count < n {
            binary = "0" + binary
        }
        
        for j in 0..<n {
            answer[i].append(binary[binary.index(binary.startIndex, offsetBy: j)] == "1" ? "#" : " ")
        }
    }
    
    return answer
}