import time

my_words = [elt.strip() for elt in open("materials/sonnet_words.txt", "r").readlines()]
word_list = [elt.strip() for elt in open("materials/sowpods.txt", "r").readlines()]
word_dict = dict((elt, 1) for elt in word_list)
word_set = set(word_list)

counter = 0

start_list = time.time()
for word in my_words:
    if word not in word_list:
        print(word)
        #counter += 1  # commented to calc just in set

end_list = time.time()
dif_list = end_list - start_list  # in seconds

start_dict = time.time()
for word in my_words:
    if word not in word_dict:
        print(word)
        #counter += 1 # commented to calc just in set

end_dict = time.time()
dif_dict = end_dict - start_dict  # in seconds

start_set = time.time()
for word in my_words:
    if word not in word_set:
        print(word)
        counter += 1

end_set = time.time()
dif_set = end_set - start_set  # in seconds

print("Total unique sonnets words: {}, done in {:.3} sec. for list, "
      "{:.3} sec for dictionary and {:.3} sec for set".format(counter, dif_list, dif_dict, dif_set))