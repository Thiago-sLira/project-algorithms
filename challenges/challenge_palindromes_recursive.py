def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    if low_index >= high_index:  # Condição de parada
        return True

    if (
        word[low_index] != word[high_index]
    ):  # Verifica os caracteres da palavra
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


word = "atata"
print(is_palindrome_recursive(word, 0, len(word) - 1))
# reversed_list = list("thiago")
# reversed_list.reverse()
# print(reversed_list)
# print("".join(reversed_list[-1]))
