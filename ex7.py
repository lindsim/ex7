import string 


def clean_file(file_path):
    our_file = open(file_path)
    word_list = []
    new_list = []
    final_list = []
    remove_these = (',.!/?~:;-"()_')
    for l in our_file:
        no_white_space = l.rstrip()
        words = no_white_space.split(' ')
        word_list = words
        for word in word_list: 
            word = word.lower()
            new_list.append(word)
    for item in new_list:
        new_item = item.translate(string.maketrans("",""), remove_these)
        final_list.append(new_item)
    return final_list


def make_dict(a_list):
    new_dictionary = {}
    for item in a_list:
        if item in new_dictionary:
            new_dictionary[item] = new_dictionary[item] + 1
        else:
            new_dictionary[item] = 1
    
    for k, v in new_dictionary.items():
        print k, v


make_dict(clean_file("twain.txt"))



