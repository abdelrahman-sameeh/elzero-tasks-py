# from 69 to 71

def my_all(list):
  for item in list:
    if not item:
      return False
  return True


# my_all
print(my_all([1, 2, 3])) # True
print(my_all([1, 2, 3, []])) # False


def my_any(list):
  for item in list:
    if item:
      return True
  return False

# my_any
print(my_any([0, 1, [], False])) # True
print(my_any([(), 0, False])) # False


def my_min(list):
  min = list[0] if list else None
  for item in list:
    if item < min:
      min = item
  return min

# # my_min
print(my_min([10, 100, -20, -100, 50])) # -100
print(my_min((10, 100, -20, -100, 50))) # -100


def my_max(list):
  max = list[0] if list else None
  for item in list:
    if item > max:
      max = item

  return max

# # my_max
print(my_max([10, 100, -20, -100, 50, 700])) # 700
print(my_max((10, 100, -20, -100, 50, 700))) # 700

print('*'*50)

# -------------------------------------------------------------------------------------


# from 72 to 75

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

# Output
# "Eman"
# "Ahmed"
# "Sameh"
# "Osama"

def remove_chars(string):
  return string[1:len(string)-1]

cleaned_names =  list(map(remove_chars, friends_map))

print(cleaned_names)

cleaned_names_with_lambda = list(map(lambda string: string[1:len(string)-1], friends_map))

print(cleaned_names_with_lambda)

print('*'*50)


# --------------------------------------------------------------------------

friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]

# Output
# "Wessam"
# "Essam"

def get_names(name):
  return name[-1] == 'm'

names = tuple(filter(get_names, friends_filter))

print(names)

names_with_lambda = tuple(filter(lambda name: name[-1]=='m', friends_filter))

print(names_with_lambda)

print('*'*50)

# --------------------------------------------------------------------------

# using reduce to get multiplying of this list 

from functools import reduce

nums = [2, 4, 6, 2]

# Output
# 96

result = reduce(lambda n1, n2: n1*n2, nums)

print(result)


print('*'*50)


# --------------------------------------------------------------------------




skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

# Output
# "50 - JavaScript"
# "52 - Python"
# "53 - PHP"
# "55 - CSS"
# "56 - HTML"

# reverse tuple
skills = skills[::-1]

for id, item in enumerate(skills, 50):
  if type(item) is not int:
    print("%d - %s" % (id, item))



print('*'*50)





