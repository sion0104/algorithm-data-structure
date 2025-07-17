def solution(mats, park):
    answer = -1
    
    mats.sort(reverse = True)
    
    for mat in mats:
        for row in range(len(park) - mat + 1):
            for col in range(len(park[row]) - mat + 1):
                
                subgrid = [park[r][col: col + mat] for r in range(row, row + mat)]
                                
                if all(all(cell == '-1' for cell in row) for row in subgrid):
                    return mat
                
    return answer

            