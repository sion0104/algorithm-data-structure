# 장르별로 2개 씩
# 노래: 고유번호

# 1. 속한 노래가 많이 재생된 장르(장르별 총 재생 횟수가 큰 순)
# 2. 해당 장르 내에서 가장 많이 재생된 음악
# 3. 횟수가 같은 경우 고유번호가 낮은 거 부터(index 번호가 낮은 것)

# 앨범에 수록될 고유번호

def solution(genres, plays):
    # 장르별 재생 횟수, 장르별 고유 번호와 재생 횟수
    total_play, genre_song = {}, {}
    
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_song[genre] = genre_song.get(genre, []) + [(index, play)]
        total_play[genre] = total_play.get(genre, 0) + play
        
    answer = []
    for genre in sorted(total_play, key=total_play.get, reverse=True): 
        answer.extend([index for index, play in sorted(genre_song[genre], key=lambda x:(-x[1], x[0]))][:2])
    
    return answer