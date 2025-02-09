def solution(arr):
    rows, cols = len(arr), len(arr[0])
    
    if rows > cols:
        for row in arr:
            row.extend([0] * (rows - cols))
    elif cols > rows:
        extra_row = [[0] * cols for _ in range(cols-rows)]
        arr.extend(extra_row)
        
    return arr