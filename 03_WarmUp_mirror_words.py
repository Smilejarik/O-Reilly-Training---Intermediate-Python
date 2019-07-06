import scrabble

max = 0
maxes = []
mir_words = []
#print longest words that are same forwards and backwards

def check_for_max(mir_words):
    global max, maxes

    for i in range(len(mir_words)):
        if len(mir_words[i]) > max:
            max = len(mir_words[i])
            index_max = i
            maxes = [i]
            print("Index of max is: " + str(index_max))
        elif len(mir_words[i]) == max:
            maxes.append(i)

    for n in maxes:
        print(mir_words[n])


"""
for word in scrabble.fonts:
    mirrorsame = True
    for index in range(len(word)):
        if word[index] != word[-(index+1)]:
            mirrorsame = False
    if mirrorsame is True:
        print(word)
        mir_words.append(word)
        print(mir_words)
"""

#second way to check if word == reversed word
for word in scrabble.fonts:

    if word == word[::-1]:  # compare to reversed version
        print(word)
        mir_words.append(word)
        print(mir_words)


check_for_max(mir_words)