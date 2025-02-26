import Foundation

func solution(_ spell:[String], _ dic:[String]) -> Int {
    let spellString = spell.sorted().joined()
    
    for word in dic {
        if spellString == String(word.sorted()) {
            return 1
        }
    }
    return 2
}
