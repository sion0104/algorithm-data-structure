def solution(dots):
    def get_slope(p1, p2):
        return (p2[1] - p1[1])/(p2[0] - p1[0])
    
    slope1to2 = get_slope(dots[0], dots[1])
    slope3to4 = get_slope(dots[2], dots[3])
    
    if slope1to2 == slope3to4:
        return 1
    
    slope2to3 = get_slope(dots[1], dots[2])
    slope1to4 = get_slope(dots[0], dots[3])
    
    if slope2to3 == slope1to4:
        return 1
    
    slope1to4 = get_slope(dots[0], dots[3])
    slope2to3 = get_slope(dots[1], dots[2])
    
    if slope1to4 == slope2to3:
        return 1
    
    return 0
          