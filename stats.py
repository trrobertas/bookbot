def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    all_characters = {}
    for char in text.lower():
        if char in all_characters:
            all_characters[char] += 1
        else:
            all_characters[char] = 1
    return all_characters

def sort_on(items):
    return items["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    letter_list = []
    for letter in num_chars_dict:
        num = num_chars_dict[letter]
        letter_list.append({"char":letter, "num":num}) 
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list