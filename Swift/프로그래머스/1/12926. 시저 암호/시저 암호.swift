func solution(_ s:String, _ n:Int) -> String {
    var result = ""
    
    for char in s {
        if char == " " {
            result.append(" ")
        } else if char.isUppercase {
            if let ascii = char.asciiValue {
                let shifted = (Int(ascii) - Int(Character("A").asciiValue!) + n) % 26
                result.append(Character(UnicodeScalar(shifted + Int(Character("A").asciiValue!))!))
            }
        } else if char.isLowercase {
            if let ascii = char.asciiValue {
                let shifted = (Int(ascii) - Int(Character("a").asciiValue!) + n) % 26
                result.append(Character(UnicodeScalar(shifted + Int(Character("a").asciiValue!))!))
            }
        }
    }
    return result
}