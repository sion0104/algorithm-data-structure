from collections import Counter

def solution(array):
    counter = Counter(array)
    
    max_count = max(counter.values())
    
    max_count_occurences = list(counter.values()).count(max_count)
    
    if max_count_occurences > 1:
        return -1
    
    for num, count in counter.items():
        if count == max_count:
            return num
        
    return -1