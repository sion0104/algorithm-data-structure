import Foundation

func solution(_ n:Int, _ k:Int) -> Int {
    var price = n * 12_000 + k * 2_000
    
    let service = n / 10
    
    if service > 0 {
        price -= service * 2_000
    }
    
    return price
}