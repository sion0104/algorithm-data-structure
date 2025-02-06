def solution(arr, flag):
    answer = []
    for index in range(len(flag)):
        if flag[index]:
            answer += (arr[index]*2) * [arr[index]]
        else:
            for _ in range(arr[index]):
                del answer[-1]
                
    return answer