import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }

var num = n[0]

for i in 1...num {
    print(String(repeating: "*", count: i))
}