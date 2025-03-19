def solution(clothes):
    categories = {}
    for cloth, category in clothes:
        if category not in categories.keys():
            categories[category] = [cloth]
        else:
            categories[category] += [cloth]
    
    answer = 1
    
    for _, value in categories.items():
        answer *= (len(value) + 1)
    
    return answer - 1