def find_duplicate(nums):
    if not nums or len(nums) == 1:
        return False
    # return True
    num_duplicate = set()
    for num in nums:
        if type(num) == str or num < 1:
            return False
        if num in num_duplicate:
            return num
        num_duplicate.add(num)
    return False


print(find_duplicate([1, 2]))
# print(type("string") == str)
