def print_upper_words(words):
    """ Print every words uppercased """
    for word in words:
        print(word.upper())




def print_upper_words2(words):
    """Print each word on line if it starts with E or e"""

    for word in words:
        if word.startswith('e') or word.startswith('E'):
        print(word.upper)



def print_upper_words3(words, must_start_with):
    """Print each word on list if it starts with given letter"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper):
                break
