def is_palindrome_recursive(word, low_index, high_index):
    if word is None:
        return False
    else:
        string_list = list(word)
        string_list.reverse()
        new_string = "".join(string_list)
        return new_string[0] == low_index and new_string[-1] == high_index
    return is_palindrome_recursive()


print(is_palindrome_recursive('socos', 's', 's'))
# reversed_list = list("thiago")
# reversed_list.reverse()
# print(reversed_list)
# print("".join(reversed_list[-1]))
