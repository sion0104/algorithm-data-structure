from itertools import permutations

def solution(word):
    words = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    def dfs(string):
        if len(string) <= 5:
            words.append(string)
            for vowel in vowels:
                dfs(string + vowel)
    
    dfs('')
    
    return words.index(word)