def solution(babbling):
    answer = 0
    possible = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        temp = word
        
        for sound in possible:
            if sound in temp:
                temp = temp.replace(sound, " ")
        
        if temp.strip() == "":
            answer += 1
    
    return answer