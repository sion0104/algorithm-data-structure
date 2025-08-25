func solution(_ x:Int) -> Bool {
    let strX = String(x)
    
    var num = 0
    
    for char in strX{
        if let digit = char.wholeNumberValue {
            num += digit
        }
    }
    
    return x % num == 0
}