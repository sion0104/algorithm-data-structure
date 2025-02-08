def solution(arr, delete_list):
    result = arr
    
    for delete in delete_list:
        if delete in result:
            result.remove(delete)
    
    return result
            