import Foundation

func solution(_ my_string:String, _ is_suffix:String) -> Int {
    if my_string.hasSuffix(is_suffix) {
        return 1
    } else {
        return 0
    }
}