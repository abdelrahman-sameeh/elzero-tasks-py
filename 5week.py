
# Needed Output

# True
# True
# True
# True
# False
# False
# False
# False

# print(bool(1))
# print(bool(1.3))
# print(bool([1]))
# print(bool((1)))
# print(bool({"1": "s"}))
# print(bool(0))
# print(bool(False))
# print(bool(None))
# print(bool([]))

#  ***********************************************************************


# html = 80
# css = 60
# javascript = 70

# # Needed Output

# print(html>50 and css>50 and javascript>50 )

#  ***********************************************************************

# num_one = 10
# num_two = 20
# num = 20

# # Needed Output


# # True
# print(num>num_one or num>num_two)
# # False
# print(num>num_one and num>num_two)


#  ***********************************************************************


# num_one = 10
# num_two = 20

# result=num_one+num_two
# print(result)
# print(result**3)

# print(result**3%26000)

# print((result**3%26000)/5)

# print(type((result**3%26000)/5))

# print(type(str((result**3%26000)/5)))


#  ***********************************************************************


# # Input
# "     osAmA   "

# # Needed Output

# "Hello Osama, Happy To See You Here."

# name = input('Enter Your Name')

# print(f"Hello {name.strip().capitalize()}, Happy To See You Here.")


#  ***********************************************************************



# while True:
#   age = input('Enter Your Age: ')
  
#   if(not age.isdigit() or int(age)<=0 ):
#     age = input('Enter a valid numeric age: ')
#   else:
#     age = int(age)
#     break
    

# if(int(age)>16):
#   print(f'Hello Your Age Is {age}, All Articles Is Suitable For You')
# else:
#   print(f'Hello Your Age Is Under 16, Some Articles Is Not Suitable For You')


#  ***********************************************************************


email = input('Enter Your Email: ')

email = email.lower().strip()
name = email.split('@')[0]
website = email.split('@')[1].split('.')[0]
domain = email.split('@')[1].split('.')[1]
# Inputs

"Osama@Nn.Sa" # Email

# Needed Output

"Your Name Is Osama"
print(f'Your Name Is {name.capitalize()}')
"Email Service Provider Is nn"
print(f'Email Service Provider Is {website}')
"Top Level Domain Is sa"
print(f'Top Level Domain Is {domain}')


