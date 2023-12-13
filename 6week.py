# # Inputs

# num1 = 20
# num2 = 40
# operation = "+" Or "-" Or "*" Or "/" Or "%"

# Needed Output

# [num1 20] [operation +] [num2]
# Example One 20 + 40 = 60
# Example Two 20 * 40 = 800

# num1= input('Enter number 1: ').strip()
# num2= input('Enter number 2: ').strip()
# operation = input('Choose Operation from these [+, -, *, /, ** it\'s mean power, %] ')

# operation_options = ['+', '-', '*', '/', '**' , '%']

# if(num1.isdigit() and num2.isdigit() and operation in operation_options ) :
#   if(operation == '+'):
#     print(f'{num1} {operation} {num2} = {int(num1) + int(num2) }')
#   elif(operation == '-'):
#     print(f'{num1} {operation} {num2} = {int(num1) - int(num2) }')
#   elif(operation == '*'):
#     print(f'{num1} {operation} {num2} = {int(num1) * int(num2) }')
#   elif(operation == '/'):
#     print(f'{num1} {operation} {num2} = {int(num1) / int(num2) }')
#   elif(operation == '%'):
#     print(f'{num1} {operation} {num2} = {int(num1) % int(num2) }')
#   elif(operation == '**'):
#     print(f'{num1} {operation} {num2} = {int(num1) ** int(num2) }')
# else:
#   print('Inputs is invalid')

# ---------------------------------------------------------------------------------

# age = 17

# # Needed Output

# "App Is Suitable For You" # If Age Larger Than 16
# "App Is Not Suitable For You" # if Age Smaller Than 16


# print("App Is Suitable For You") if age > 16 else print("App Is Not Suitable For You") 

# ---------------------------------------------------------------------------------


# Input Example 38

# # Needed Output
# "Your Age In Months Is 456 Months" # Months Example
# "Your Age In Weeks Is 1824 Weeks" # Weeks Example

# age = input('Enter Your Age: ')

# if(age.isdigit()):
#   if(int(age)>10 and int(age)<100 ):
#     print(f'Your Age In Months Is {int(age)*12} Months')
#     print(f'Your Age In Weeks Is {int(age)*12*4} Weeks')
#     print(f'Your Age In Days Is {int(age)*365} Days')
#     print(f'Your Age In Hours Is {int(age)*365*24} Hours')
#     print(f'Your Age In Minutes Is {int(age)*365*24*60} Minutes')
#     print(f'Your Age In Seconds Is {int(age)*365*24*60*60} Seconds')
    
#   else:
#     print('Not allowed for u')
    
    
# ---------------------------------------------------------------------------------



# Input Example One "Egypt"
# Input Example Two "Ghana"

# country = input("Input Your Country ").strip().capitalize()
# countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "Bahrain"]
# price = 100
# discount = 30

# # # Needed Output
# # "Your Country Eligible For Discount And The Price After Discount Is $70" # Egypt Example
# # "Your Country Not Eligible For Discount And The Price Is $100" # Ghana Example

# if(country in countries):
#   print(f"Your Country Eligible For Discount And The Price After Discount Is ${price-discount}")
# else:
#   print(f"Your Country Not Eligible For Discount And The Price Is ${price}")




