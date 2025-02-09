import Foundation

func solution(_ picture:[String], _ k:Int) -> [String] {
    var answer = [String]()
    
    for line in picture {
        var pixels = ""
        
        for pixel in line {
            pixels += String(repeating: pixel, count: k)
        }
        
        for _ in 0..<k {
           answer.append(pixels) 
        }
    } 
    return answer
}