import scrabble

text = "ka"
#print all words containing "text"
for word in scrabble.fonts:
    if text in word:
        print(word)

#print letters that are not doubled
import string

alphabet = string.ascii_lowercase
print(alphabet)

for letter in alphabet:
    print("Next letter is: " + letter)
    exists = False
    for word in scrabble.fonts:
        if str(letter + letter) in word:
            print("This letter " + letter + " is double in: " + word)
            exists = False
            break
        else:
            exists = True

    if exists is True:
        print("No double for letter: " + letter)