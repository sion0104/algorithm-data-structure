# 번호: 체격 순
# 번호 - 1, 번호, 번호 + 1

# 전체 학생 수, 도난 학생 번호, 여벌 체육복 학생 번호
def solution(n, lost, reserve):
    real_lost = set(lost) - set(reserve)
    real_reserve = set(reserve) - set(lost)
    
    for student in real_lost:            
        if student-1 in real_reserve:
            real_reserve.remove(student-1)
        elif student+1 in real_reserve:
            real_reserve.remove(student+1)
        else:
            n -= 1
    
    return n
    # 반환값: 체육 수업을 들을 수 있는 학생의 최댓값