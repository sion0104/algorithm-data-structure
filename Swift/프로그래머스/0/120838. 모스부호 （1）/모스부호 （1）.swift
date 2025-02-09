import Foundation

func solution(_ letter:String) -> String {
    
    let morse: [String: String] = [
        ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f",
        "--.": "g", "....": "h", "..": "i", ".---": "j", "-.-": "k", ".-..": "l",
        "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r",
        "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x",
        "-.--": "y", "--..": "z"
    ]
    
    var answer = ""
    let morses = letter.split(separator: " ")
    
    for char in morses {
        if let letter = morse[String(char)] {
            answer += letter
        }
    }
    return answer
}