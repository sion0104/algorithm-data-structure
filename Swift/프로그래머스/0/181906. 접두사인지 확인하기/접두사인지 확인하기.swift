import Foundation

func solution(_ my_string:String, _ is_prefix:String) -> Int {
    if my_string.hasPrefix(is_prefix) {
        return 1
    }
    return 0
}