# 차량의 경로, 최소 설치 개수

# [진입 지점, 나간 지점]
def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    camera = routes[0][1]
    camera_count = 1
    
    for route in routes[1:]:
        if camera < route[0]:
            camera = route[1]
            camera_count += 1
        
    return camera_count
    
        
        