S="aeioup??"
vowels = 'aeiou'
vowel_count = 0
consonant_count = 0

for char in S:

    if char == '?':
        vowel_count += 1
        consonant_count += 1

    elif char in vowels:
        vowel_count += 1
        consonant_count = 0

    else:
        consonant_count += 1
        vowel_count = 0

    if consonant_count == 4 or vowel_count == 6:
        print (0)

print (1)