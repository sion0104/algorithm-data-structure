def solution(babbling):
    count = 0
    
    for word in babbling:
        word = word.replace("aya", "1")\
                .replace("ye", "2")\
                .replace("woo", "3")\
                .replace("ma", "4")
        
        if word.isdigit():
            if not any(str(i) + str(i) in word for i in range(1, 5)):
                count += 1
        
    return count