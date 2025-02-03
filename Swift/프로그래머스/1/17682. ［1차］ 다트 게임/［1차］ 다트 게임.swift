import Foundation

func solution(_ dartResult: String) -> Int {
    do {
        // 정규표현식 패턴: (숫자)(보너스[SDT])(옵션[*#]?)
        let pattern = "(\\d+)([SDT])([*#]?)"
        let regex = try NSRegularExpression(pattern: pattern)
        let nsRange = NSRange(dartResult.startIndex..<dartResult.endIndex, in: dartResult)
        // 정규표현식과 일치하는 모든 부분을 찾음
        let matches = regex.matches(in: dartResult, range: nsRange)

        // 각 라운드의 점수를 저장할 배열
        var scores: [Int] = []

        for match in matches {
            // 각 그룹에 해당하는 문자열 추출
            let scoreRange = Range(match.range(at: 1), in: dartResult)!
            let bonusRange = Range(match.range(at: 2), in: dartResult)!
            let optionRange = match.range(at: 3).location != NSNotFound ? Range(match.range(at: 3), in: dartResult) : nil

            // 점수, 보너스, 옵션 파싱
            let score = Int(dartResult[scoreRange])!
            let bonus = dartResult[bonusRange]
            let option = optionRange != nil ? dartResult[optionRange!] : ""

            // 최종 점수 계산
            var finalScore = score
            
            // 보너스(S,D,T) 적용
            switch bonus {
            case "S": // Single: 1제곱
                finalScore = Int(pow(Double(score), 1))
            case "D": // Double: 2제곱
                finalScore = Int(pow(Double(score), 2))
            case "T": // Triple: 3제곱
                finalScore = Int(pow(Double(score), 3))
            default:
                break
            }

            // 옵션(*,#) 적용
            if option == "*" { // 스타상: 해당 점수와 직전 점수 2배
                if let prevIndex = scores.indices.last {
                    scores[prevIndex] *= 2
                }
                finalScore *= 2
            } else if option == "#" { // 아차상: 해당 점수 마이너스
                finalScore *= -1
            }

            // 계산된 점수를 배열에 추가
            scores.append(finalScore)
        }

        // 모든 라운드의 점수 합계 반환
        return scores.reduce(0, +)
    } catch {
        return 0 // 정규표현식 처리 중 오류 발생 시 0 반환
    }
}
