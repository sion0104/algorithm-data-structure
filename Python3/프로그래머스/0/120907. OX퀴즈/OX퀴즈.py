def solution(quiz):
    answer = []
    
    for operation in quiz:
        operation_array = operation.split(" ")
        
        num1, operation, num2, num_answer = int(operation_array[0]), operation_array[1], int(operation_array[2]), int(operation_array[4])
        
        guess = 0
        
        if operation == "+":
            guess = num1 + num2
        else:
            guess = num1 - num2
        
        if guess == num_answer:
            answer.append("O")
        else:
            answer.append("X")
            
    return answer