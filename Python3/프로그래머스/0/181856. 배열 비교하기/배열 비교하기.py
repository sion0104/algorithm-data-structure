def solution(arr1, arr2):
    arr1Score, arr2Score = len(arr1), len(arr2)
    
    while True:
        if arr1Score > arr2Score:
            return 1
        elif arr1Score < arr2Score:
            return -1
        else:
            arr1Score, arr2Score = sum(arr1), sum(arr2)
        
        if arr1Score == arr2Score:
            return 0
        