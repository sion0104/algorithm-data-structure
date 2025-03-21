def solution(answers):
    answer1 = [1, 2, 3, 4, 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        if answer1[i % len(answer1)] == answer:
            score[0] += 1
        if answer2[i % len(answer2)] == answer:
            score[1] += 1
        if answer3[i % len(answer3)] == answer:
            score[2] += 1
        
    # 반환값: 가장 많이 문제를 맞춘 사람의 번호 배열
    max_score = max(score)
    return [i + 1 for i in range(len(score)) if score[i] == max_score]
            