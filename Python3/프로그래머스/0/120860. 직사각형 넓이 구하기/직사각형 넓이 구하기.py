def solution(dots):
    x_coordinates = [dot[0] for dot in dots]
    y_coordinates = [dot[1] for dot in dots]
    
    width = max(x_coordinates) - min(x_coordinates)
    height = max(y_coordinates) - min(y_coordinates)
    
    return width * height