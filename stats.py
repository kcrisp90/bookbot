def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    counts = {}
    for char in text.lower():
        if char.isalpha() or char.isnumeric():  # only count letters and digits
            counts[char] = counts.get(char, 0) + 1
    return counts

def sort_char_counts(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        sorted_list.append({"char": char, "num": count})
    
    def sort_by_num(item):
        return item["num"]
    
    sorted_list.sort(key=sort_by_num, reverse=True)
    return sorted_list