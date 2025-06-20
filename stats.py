def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def num_words(text):
    return len(text.split())

def get_number_of_characters(text):
    characters = {}
    for i in range(len(text)):
        char = text[i].lower()
        if(char in characters):
            characters[char] += 1
        else: 
            characters[char] = 1

    return characters

# returns num key to tell sort how which key to sort.
def sort_on(dict):
    return dict["num"]


def sort_dictionary(dict):
    ordered_list = []
    for key in dict:
        ordered_list.append({"char": key, "num": dict[key]}) 
    
    ordered_list.sort(reverse=True, key=sort_on)
    return ordered_list
