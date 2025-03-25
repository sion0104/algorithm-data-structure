from collections import Counter

def solution(A, B):
    if A == B:
        return 0
    
    if Counter(A) == Counter(B):
        newA = A[-1] + A [0: len(A)-1]
        count = 1
        # print(newA)
        
        for _ in range(len(A)):
            if newA == B:
                return count

            newA = newA[-1] + newA[0:len(A)-1]
            count += 1
            # print(count, newA)
    return -1