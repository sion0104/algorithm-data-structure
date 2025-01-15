import Foundation

import Foundation

extension String {
    func swapcase() -> String {
        return self.map { character in
            let strChar = String(character)
            if strChar == strChar.uppercased() {
                return strChar.lowercased()
            } else {
                return strChar.uppercased()
            }
        }.joined()
    }
}

let s1 = readLine()!
print(s1.swapcase())