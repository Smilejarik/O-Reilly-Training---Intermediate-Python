my_words = [elt.strip() for elt in open("materials/sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("materials/sowpods.txt", "r").readlines()]

counter = 0

for word in my_words:
    if word not in word_list:
        print(word)
        counter += 1

print("Total unique sonnets words: {}".format(counter))