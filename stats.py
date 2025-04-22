def get_num_words(words):
    seperated_words = words.split()
    count = 0

    for i in seperated_words:
        count+=1

    return count

def get_num_chars(words):
    char_counts = {}
    for char in words:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(chars_dict):
    # Create a list of dictionaries with charcter and count
    chars_list = []
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Sort the list by count in descending order
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list