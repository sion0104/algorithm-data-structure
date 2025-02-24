def solution(n, arr1, arr2):
    answer = ["" for _ in range(n)]
    
    for i in range(n):
        binary = str(bin(arr1[i] | arr2[i]))
        binary = binary.lstrip("0b")
    
        while len(binary) < n:
            binary = "0" + binary
            
        for j in range(n):
            answer[i] += "#" if binary[j] == "1" else " "
    
    return answer