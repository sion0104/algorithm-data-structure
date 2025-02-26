def solution(spell, dic):
    spell_string = ''.join(sorted(spell))
    
    for word in dic:
        if spell_string == ''.join(sorted(word)):
            return 1
    
    return 2