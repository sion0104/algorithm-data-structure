def solution(array, commands):
    answer = []
    for a, b, num in commands:
        answer.append(sorted(array[a-1:b])[num-1])
    return answer
        