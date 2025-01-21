def solution(arr, queries):
    answer = []
    
    for i, j, k in queries:
        temp = arr[i:j+1]
        
        filtered = sorted([x for x in temp if x > k])
        
        if not filtered:
            answer.append(-1)
        else:
            answer.append(filtered[0])
    
    return answer

            
            
