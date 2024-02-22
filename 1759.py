from itertools import combinations

L, C = map(int, input().split())
alphabets = input().split()

passwords = combinations(sorted(alphabets), L)
answer = []

for password in passwords:
    vowel_count, consonant_count = 0, 0

    for alphabet in password:
        if alphabet in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        else:
            consonant_count += 1

    if vowel_count >= 1 and consonant_count >= 2:
        print("".join(password))
