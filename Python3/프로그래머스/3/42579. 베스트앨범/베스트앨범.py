def solution(genres, plays):
    songs = {}
    total_plays = {}
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in songs:
            songs[genre] = []
        songs[genre].append((i, play))
        total_plays[genre] = total_plays.get(genre, 0) + play
        
    answer = []
    for genre in sorted(total_plays, key=total_plays.get, reverse=True):
        for i in sorted(songs[genre], key=lambda x: (-x[1], x[0]))[:2]:
            answer.append(i[0])
    
    return answer