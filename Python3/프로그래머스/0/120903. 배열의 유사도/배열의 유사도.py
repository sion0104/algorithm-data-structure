def solution(s1, s2):
    set1, set2 = set(s1), set(s2)
    common_elements = set1 & set2
    
    return len(common_elements)