import Foundation

func solution(_ myStr:String) -> [String] {
    let splitByA = myStr.split(separator: "a")
    let splitByB = splitByA.flatMap{ $0.split(separator: "b") }
    let splitByC = splitByB.flatMap{ $0.split(separator: "c") }
    
    let result = splitByC.map{ String($0) }.filter{ !$0.isEmpty }
    
    if result.isEmpty {
        return ["EMPTY"]
    }
    
    return result
}