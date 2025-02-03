def solution(dartResult):
    import re
    
    pattern = re.compile(r'(\d+)([SDT])([*#]?)')
    dart_parsed = pattern.findall(dartResult)

    scores = []

    for i, (score, bonus, option) in enumerate(dart_parsed):
        score = int(score)
        if bonus == 'S':
            score = score ** 1
        elif bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
        
        if option == '*':
            score *= 2
            if i > 0:
                scores[i-1] *= 2
        elif option == '#':
            score *= -1
        
        scores.append(score)
    
    return sum(scores)