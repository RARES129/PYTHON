def is_vowel(char):
    if char in "aeiouAEIOU":
        return True


word = input()
vowel_count = 0
for char in word:
    if is_vowel(char):
        vowel_count += 1
print(vowel_count)
