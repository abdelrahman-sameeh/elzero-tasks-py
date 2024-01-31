# # from-86-to-89


# my_list = ["E", "Z", "R", 1, 2, 3]
# my_tuple = ("L", "E", "O")
# my_data = []

# for data in zip(my_list, my_tuple):
#   my_data.append(data[0])
#   my_data.append(data[1])
  

# print("".join(my_data).capitalize()) # Elzero

# print('*'*50)

# # ----------------------------------------------------------------------------
# my_list1 = ["E", "L", "Z", "E", "R", "O", 1, 2]
# my_tuple = ("E", "Z", "R", 1, 2, "E", "R", "O")
# my_list2 = ("L", "E", "O", 1, 2, "E", "R", "O")
# my_data = []

# for item1, item2, item3 in zip(my_list1, my_tuple, my_list2):
#   # Write Your Code Here
#   if type(item1) is str:
#     my_data.append(item1)

# print("".join(my_data).capitalize())




# print('*'*50)

# # ----------------------------------------------------------------------------


# #### hist #### dont forget to install pillow  ====> pip install -user pillow
# # from PIL import Image

# # image_path = './elzero-pillow.png'

# # image = Image.open(image_path)

# # # image.show()

# # # crop image
# # box = (400, 0, 800, 400)

# # L_image = image.crop(box).convert('L')

# # L_image.save("L_image.png")  

# # L_image.show()

# # Row_image = image.crop((0, 400, 1200, 800)).convert('L').rotate(180)


# # Row_image.save("Row_image.png")  

# # Row_image.show()


# print('*'*50)

# # ----------------------------------------------------------------------------

# # Write Function With Help To Get The Output

# def say_hello_to(name):
#   """
#   parameter(someone) => Person Name
#   Function To Say Hello To Anyone
#   """
#   return f"Hello {name}"
  
# print(say_hello_to("Osama")) # "Hello Osama"


# print(say_hello_to.__doc__)
# # or 
# help(say_hello_to)

# # Write Doc String Line For The Function Here

# # Function Doc String Output
# # "parameter(someone) => Person Name"
# # "Function To Say Hello To Anyone"



# print('*'*50)

# ----------------------------------------------------------------------------

# show pylint_update_module.py file
myFriends = ["Ahmed", "Osama", "Sayed"]

def sayHello(SomePeoples) -> list:
  """
  this is a doc string for this function
  """
  for Someone in SomePeoples:
    print(f"Hello {Someone}")

sayHello(myFriends)


print('*'*50)

# ----------------------------------------------------------------------------

# from-90-to-94/

# NUM = input("Add Your Number ")

# # Your Code Here

# if len(NUM)>1:
#   raise IndexError('Only One Character Allowed')
# elif(type(NUM) is int):
#   print("#"*20, "\n", f"The Number Is {NUM}", '\n', '#'*20)
# elif NUM=='0':
#   raise ValueError('Number Must Be Larger Than 0')
# else:
#   raise('Only Numbers Allowed')



# print('*'*50)

# ----------------------------------------------------------------------------



# # Your Code Here
# LETTER = input("Add Letter From A to Z :")
# try:
#   if len(LETTER) >1:
#     raise ValueError("You Must Write One Character Only")
#   elif( "a"<= LETTER <="z"):
#     raise Exception("You Must Write One Small Letter From 'a' to 'z'")
# except ValueError as ve :
#   print(f'Error {ve}')
# except Exception as e:
#   print(f'Error {e}')
# else:
#   print(f"You Typed {LETTER}")


# print('*'*50)

# ----------------------------------------------------------------------------




def calculate(num1:int, num2:int) -> int:
  return num1 + num2

print(calculate(20, 30))