# 대기 큐
# 1. 우선 순위(소요시간 짧은 것, 작업 시간의 요청 시각이 빠른 것, 작업 번호가 작은 것 순)
# 마칠 때까지 그 작업만 수행

# index: 작업 번호[작업 요청 시각, 소요 시간]
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
        
        