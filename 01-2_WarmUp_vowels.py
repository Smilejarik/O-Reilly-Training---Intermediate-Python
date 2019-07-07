import scrabble

vowels = "qwert"

#print all words that contain all vowels
def has_all_vowels(word):
    contains = True
    for vowel in vowels:
        if vowel not in word:
            contains = False
    return contains


for word in scrabble.fonts:
    if has_all_vowels(word):
        print(word)