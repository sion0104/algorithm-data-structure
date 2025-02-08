def solution(date1, date2):
    for index in range(len(date1)):
        if date1[index] < date2[index]:
            return 1
        elif date1[index] > date2[index]:
            return 0
    
    return 0