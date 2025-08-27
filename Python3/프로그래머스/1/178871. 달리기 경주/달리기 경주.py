def solution(players, callings):
    answer = {player: i for i, player in enumerate(players)}
    
    for i in callings:
        index = answer[i]
        answer[i] -= 1
        answer[players[index-1]] += 1
        players[index - 1], players[index] = players[index], players[index-1]
        
    return players