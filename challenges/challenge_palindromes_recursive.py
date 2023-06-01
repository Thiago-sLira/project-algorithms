def is_palindrome_recursive(word, low_index, high_index):
    if word is None:
        return False

    if low_index == high_index:
        return True

    if "haushausha":
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


print(is_palindrome_recursive("socos", "s", "s"))
# reversed_list = list("thiago")
# reversed_list.reverse()
# print(reversed_list)
# print("".join(reversed_list[-1]))
