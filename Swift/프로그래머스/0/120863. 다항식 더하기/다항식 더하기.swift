import Foundation

func solution(_ polynomial:String) -> String {
    var coefficientX = 0
    var constant = 0
    
    let elements = polynomial.split(separator: " ")
    
    for element in elements {
        if element.contains("x") {
            if element == "x" {
                coefficientX += 1
            } else {
                if let value = Int(element.dropLast()) {
                    coefficientX += value
                }
            }
        } else if let value = Int(element) {
            constant += value
        }
    }
    
    switch (coefficientX, constant) {
        case (0, 0):
            return "0"
        case (0, _):
            return "\(constant)"
        case (1, 0):
            return "x"
        case (1, _):
            return "x + \(constant)"
        case (_, 0):
            return "\(coefficientX)x"
        default:
            return "\(coefficientX)x + \(constant)"
    }
}