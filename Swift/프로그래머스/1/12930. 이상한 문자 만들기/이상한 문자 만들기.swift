func solution(_ s:String) -> String {
    var result = ""
    var wordIndex = -1
    
    for char in s {
        if char == " " {
            result.append(char)
            wordIndex = -1  // 공백을 만나면 단어 인덱스 초기화
        } else {
            wordIndex += 1
            if wordIndex % 2 == 0 {
                result.append(String(char).uppercased())
            } else {
                result.append(String(char).lowercased())
            }
        }
    }
    
    return result
}