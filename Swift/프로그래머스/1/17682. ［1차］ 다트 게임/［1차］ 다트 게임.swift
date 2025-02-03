import Foundation

func solution(_ dartResult: String) -> Int {
    do {
        let pattern = "(\\d+)([SDT])([*#]?)"
        let regex = try NSRegularExpression(pattern: pattern)
        let nsRange = NSRange(dartResult.startIndex..<dartResult.endIndex, in: dartResult)
        let matches = regex.matches(in: dartResult, range: nsRange)

        var scores: [Int] = []

        for match in matches {
            let scoreRange = Range(match.range(at: 1), in: dartResult)!
            let bonusRange = Range(match.range(at: 2), in: dartResult)!
            let optionRange = match.range(at: 3).location != NSNotFound ? Range(match.range(at: 3), in: dartResult) : nil

            let score = Int(dartResult[scoreRange])!
            let bonus = dartResult[bonusRange]
            let option = optionRange != nil ? dartResult[optionRange!] : ""

            var finalScore = score
            switch bonus {
            case "S":
                finalScore = Int(pow(Double(score), 1))
            case "D":
                finalScore = Int(pow(Double(score), 2))
            case "T":
                finalScore = Int(pow(Double(score), 3))
            default:
                break
            }

            if option == "*" {
                if let prevIndex = scores.indices.last {
                    scores[prevIndex] *= 2
                }
                finalScore *= 2
            } else if option == "#" {
                finalScore *= -1
            }

            scores.append(finalScore)
        }

        return scores.reduce(0, +)
    } catch {
        return 0
    }
}