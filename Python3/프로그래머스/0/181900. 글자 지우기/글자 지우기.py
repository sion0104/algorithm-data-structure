def solution(my_string, indices):
    array = list(my_string)
    for i in indices:
        array[i] = "0"
        
    while "0" in array:
        array.remove("0")
        
    return "".join(array)