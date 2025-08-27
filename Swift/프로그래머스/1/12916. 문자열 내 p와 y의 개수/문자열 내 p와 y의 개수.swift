import Foundation

func solution(_ s:String) -> Bool
{
    let lower = s.lowercased()
    
    let countP = lower.filter { $0 == "p" }.count
    let countY = lower.filter { $0 == "y" }.count
    
    return countP == countY
}