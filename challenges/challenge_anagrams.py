def merge_sort(string):
    if len(string) <= 1:
        return string.lower() or ""

    string_lower = string.lower()
    mid = len(string) // 2
    left = merge_sort(string_lower[:mid])
    right = merge_sort(string_lower[mid:])

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return "".join(merged)


def is_anagram(first_string, second_string):
    first_string_sorted = merge_sort(first_string)
    second_string_sorted = merge_sort(second_string)

    if len(first_string) == 0 or len(second_string) == 0:
        return (
            first_string_sorted,
            second_string_sorted,
            False,
        )

    return (
        first_string_sorted,
        second_string_sorted,
        first_string_sorted == second_string_sorted,
    )


# word1 = "muro"
# # word1_in_list = list(word1)
# word2 = ""

# # print(merge_sort(word1) == merge_sort(word2))
# print(is_anagram(word1, word2))
# print(word2.lower())
