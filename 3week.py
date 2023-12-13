# # num = 1+2j

# # print(num.imag)
# # print(num.real)

# # **************************************************************************************

# num = 10

# # Needed Output
# # 10.0000000000

# print(f"{num:.10f}")

# # **************************************************************************************
# num = 159.650

# # Needed Output
# # 159
# # <class 'int'>

# print(int(num))
# print(type( int(num)))

# # **************************************************************************************

# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# # "Osama" => Method One
# # "Osama" => Method Two
# # "Mahmoud" => Method One
# # "Mahmoud" => Method Two

# print(friends[0])

# print(friends[-1])
# print(friends[len(friends)-1])
# print(friends.pop())



# # **************************************************************************************


# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# # "Osama", "Sayed", "Mahmoud"
# # "Ahmed", "Ali"
# print(friends[0], friends[2], friends[4])
# print(friends[1], friends[3])

# # **************************************************************************************


# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# # "Ahmed", "Sayed", "Ali",
# # "Ali", "Mahmoud"

# print(', '.join( friends[1:-1]))
# print(', '.join(friends[-2:]))

# # **************************************************************************************


# friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# # Needed Output
# # ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]

# friends[-1]='Elzero'
# friends[-2]='Elzero'

# print(friends)


# # **************************************************************************************

# friends = ["Osama", "Ahmed", "Sayed"]

# # Needed Output
# # ["Nasser", "Osama", "Ahmed", "Sayed"]
# # ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# friends.insert(0, 'Nasser')
# friends.append('Salem')

# print(friends)

# # **************************************************************************************

# friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

# # Needed Output
# # ["Ahmed", "Sayed", "Salem"]
# # ["Ahmed", "Sayed"]

# friends = friends[2:]
# print(friends)
# friends = friends[:-1]
# print(friends)

# # **************************************************************************************



# friends = ["Ahmed", "Sayed"]
# employees = ["Samah", "Eman"]
# school = ["Ramy", "Shady"]


# # friends += employees + school
# friends.extend(employees + school)
# print(friends)


# # **************************************************************************************


# friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

# # Needed Output
# friends.sort()
# print(friends)
# # ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
# friends.sort(reverse=True)
# print(friends)
# # ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']


# # **************************************************************************************


# # Needed Output

# # "Osama"
# # <class 'tuple'>

# my_tuple = 'Osama',
# print(my_tuple)
# print(type(my_tuple))

# # **************************************************************************************


# friends = ("Osama", "Ahmed", "Sayed")

# # Needed Output Change Osama to Elzero

# # ("Elzero", "Ahmed", "Sayed")
# # <class 'tuple'>
# # 3 Elements

# friends = list(friends)

# friends[0] = 'Elzero'

# friends = tuple(friends)

# print(friends)
# print(type(friends))
# print(f"{len(friends)} Elements")



# # **************************************************************************************

# nums = (1, 2, 3)
# letters = ("A", "B", "C")

# # Needed Output


# # nums_and_letters_one = (1, 2, 3, "A", "B", "C")
# # 6 Elements

# new_tuple = nums + letters

# print(new_tuple)
# print(f"{len(new_tuple)} Elements")


# # **************************************************************************************



my_tuple = (1, 2, 3, 4)

# Needed Output

# 1
# 2
# 4


a, b, *rest = my_tuple

print(a)
print(b)
print(rest[-1])


# or 

a, b, _, c = my_tuple

print(a)
print(b)
print(c)
