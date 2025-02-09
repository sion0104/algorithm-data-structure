def solution(myString):
    alphabet = "abcdefghijk"
    my_string_list = list(myString)
    
    for index in range(len(my_string_list)):
        if my_string_list[index] in alphabet:
            my_string_list[index] = "l"
    
    return "".join(my_string_list)