# 한 번씩만 변환
# words에 포함된 단어
# begin -> target

# 최소 과정 구하기(BFS)
# 변환할 수 없는 경우 0 return
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])
    visited = set()
    
    
    while queue:
        current, count = queue.popleft()
        
        if current == target:
            return count
        
        for word in words:
            if can_change(current, word) and word not in visited:
                queue.append((word, count + 1))
                visited.add(word)
    return 0

def can_change(word1, word2):
    diff = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            diff += 1
    
    return diff == 1