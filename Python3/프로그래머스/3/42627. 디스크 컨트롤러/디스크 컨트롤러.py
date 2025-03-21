# 대기큐: [작업 번호, 요청 시각, 소요 시간]
# 처음은 empty

# 우선순위 순으로 작업 수행
# 소요 시간 짧은 것 -> 작업 요청 시각 -> 작업 번호 작은 것

# jobs [요청 시점, 소요 시간] index: 작업 번호
import heapq

def solution(jobs):
    jobs.sort()
    length = len(jobs)
    current_time = 0
    total_time = 0
    waiting = []
    job_index = 0
    
    while job_index < length or waiting:
        while job_index < length and jobs[job_index][0] <= current_time:
            heapq.heappush(waiting, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        
        if waiting:
            duration, request_time = heapq.heappop(waiting)
            current_time += duration
            total_time += (current_time - request_time)
        else:
            if job_index < length:
                current_time = jobs[job_index][0]
        
    return total_time // length
# 반환값: 반환 시간의 평균의 정수 부분
# 반환 시간 : 작업 요청부터 종료까지 걸린 시간