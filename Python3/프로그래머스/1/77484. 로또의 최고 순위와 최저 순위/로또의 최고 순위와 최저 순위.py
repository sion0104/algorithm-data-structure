def solution(lottos, win_nums):
    count = 0
    answer = []
    
    for win_num in win_nums:
        if win_num == 0:
            continue
        if win_num in lottos :
            count += 1
            
    if count > 1:
        answer.append(7-count)
    else:
        answer.append(6)
    
    zero_count = lottos.count(0)
    if zero_count + count > 1:
        answer.append(7-zero_count-count)
    else:
        answer.append(6)
        
    return sorted(answer)
    