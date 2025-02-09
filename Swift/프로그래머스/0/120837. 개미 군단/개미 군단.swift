import Foundation

func solution(_ hp:Int) -> Int {
    let generals = hp / 5
    var remainder = hp % 5
    
    let soldiers = remainder / 3
    remainder = remainder % 3
    
    let workers = remainder
    
    return generals + soldiers + workers
}