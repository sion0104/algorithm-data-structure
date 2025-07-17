import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var left: Int64 = 1
    var right: Int64 = Int64(times.max()!) * Int64(n)
    
    var answer:Int64 = 0
    
    while left <= right {
        var mid = (left + right) / 2
        var people: Int64 = 0
        
        for time in times {
            people += Int64(mid / Int64(time) )
            
            if people >= n {
                break
            }
        }
        
        if people >= n {
            answer = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    
    return Int64(answer)
}