import time

my_words = [elt.strip() for elt in open("materials/sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("materials/sowpods.txt", "r").readlines()]
word_dict = dict((elt, 1) for elt in word_list)
word_set = set(word_list)

print("Some lovely: {}".format([elt.strip("w") for elt in my_words if "love" in elt.lower()]))  # show element striped(w) for elt in sonnet words if "love" is in word

print("Mirrored words: {}".format([elt for elt in my_words if elt == elt[::-1]]))  # show element (word) if word can be mirrored

squares_list = [elt*elt for elt in range(11) if int(elt) <= 7]
print("Squares are: {}".format(squares_list))  # print squares if element in range <=7