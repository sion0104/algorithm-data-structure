def solution(a, b):
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    num = sum(month[0:a-1]) + b

    
    return week[num % len(week) - 1]