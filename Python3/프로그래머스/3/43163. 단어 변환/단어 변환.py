from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set() 
    
    while queue:
        current, steps = queue.popleft()
        
        if current == target:
            return steps
        
        for word in words:
            if word not in visited and can_change(current, word):
                visited.add(word)
                queue.append((word, steps + 1))
                
    return 0
    
def can_change(word1, word2):
    diff = 0
    
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff += 1
    
    return diff == 1