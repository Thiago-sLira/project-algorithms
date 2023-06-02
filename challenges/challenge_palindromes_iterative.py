def is_palindrome_iterative(word):
    if word is None or len(word) == 0:
        return False
    else:
        string_list = list(word)
        string_list.reverse()
        new_string = "".join(string_list)
        return new_string == word
