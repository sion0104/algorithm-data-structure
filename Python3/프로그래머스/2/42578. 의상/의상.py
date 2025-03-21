def solution(clothes):
    categories = {}
    
    for name, category in clothes:
        categories[category] = categories.get(category, []) + [name]
        
    answer = 1
    
    for value in categories.values():
        answer *= len(value) + 1
    
    return answer - 1
        