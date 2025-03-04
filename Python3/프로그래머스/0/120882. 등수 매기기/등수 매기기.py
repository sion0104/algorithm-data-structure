def solution(score):
    averages = [sum(s)/2 for s in score]
    
    ranks = []
    for avg in averages:
        rank = 1 + sum(a > avg for a in averages)
        ranks.append(rank)
        
    return ranks