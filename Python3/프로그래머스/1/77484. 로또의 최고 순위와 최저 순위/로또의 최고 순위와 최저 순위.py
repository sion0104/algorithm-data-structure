def solution(lottos, win_nums):
    count = 0
    
    for win_num in win_nums:
        if win_num in lottos :
            count += 1
    
    zero_count = lottos.count(0)
    
    maxRank = min(6, 7-(zero_count + count))
    
    minRank = min(6, 7-count)

        
    return [maxRank, minRank]
    