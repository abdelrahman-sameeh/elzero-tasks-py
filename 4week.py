# my_list = [1, 2, 3, 3, 4, 5, 1]
# # Needed Output

# # 1, 2, 3, 4, 5
# # <class 'list'>
# # 1, 2, 3, 4


# unique_list = list(set(my_list))

# print(unique_list)

# ---------------------------------------------------------

# nums = {1, 2, 3}
# letters = {"A", "B", "C"}

# my_set = nums.union(letters)
# print(my_set)
# my_set = nums | letters
# print(my_set)
# nums.update(*letters)
# my_set = nums
# print(my_set)


# ---------------------------------------------------------

# my_set = {1, 2, 3}
# letters = {"A", "B", "C"}
# # Needed Output

# letters_list = list(letters)
# A_B = [el for el in letters_list if el in {'A', 'B'}]


# # {1, 2, 3}
# # set()
# # {"A", "B"}

# print(my_set)
# my_set.clear()
# print(my_set)
# my_set.update( set(A_B) )
# print(my_set)

# print(my_set.discard('C'))


# ---------------------------------------------------------

# set_one = {1, 2, 3}
# set_two = {1, 2, 3, 4, 5, 6}

# print(set_one.issubset(set_two))


