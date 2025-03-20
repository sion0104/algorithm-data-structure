def solution(answers):
    # 1, 2, 3, 4, 5
    # 2, 1, 2, 3, 2, 4, 2, 5
    # 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
    
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    for i, answer in enumerate(answers):
        if first[i % len(first)] == answers[i]:
            scores[0] += 1
        if second[i % len(second)] == answers[i]:
            scores[1] += 1
        if third[i % len(third)] == answers[i]:
            scores[2] += 1
            
    max_score = max(scores)
    result = [i + 1 for i in range(len(scores)) if scores[i] == max_score]
    
    return result