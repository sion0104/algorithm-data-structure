import Foundation

func solution(_ chicken:Int) -> Int {
    var chickens = chicken / 10
    var coupons = chicken % 10
    var prev_chickens = chickens
    
    while true {
        coupons += prev_chickens
        chickens += coupons / 10
        prev_chickens = coupons / 10
        coupons = coupons % 10
        
        if prev_chickens + coupons < 10 {
            break
        }
    }
    return chickens
}