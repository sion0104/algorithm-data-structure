def solution(arr, query):    
    for index in range(len(query)):
        if index % 2 == 0:
            del arr[query[index]+1:]
        else :
            del arr[:query[index]]
    
    return arr