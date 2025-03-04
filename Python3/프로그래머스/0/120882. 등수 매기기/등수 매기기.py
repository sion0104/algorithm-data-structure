def solution(score):
    avg_list = [(sum(s)/2, i) for i, s in enumerate(score)]
    avg_list.sort(reverse= True)
    
    ranks = [0] * len(score)
    cur_rank = 1
    prev_score = None
    same_rank_count = 0
    
    for avg, idx in avg_list:
        if prev_score != avg:
            cur_rank += same_rank_count
            same_rank_count = 1
        else:
            same_rank_count += 1
        ranks[idx] = cur_rank
        prev_score = avg
        
    return ranks