# Output  =>  "Hello 'Osama', How You Doing \ """ Your Age Is "38"" + And Your Country Is: Egypt
name= 'abdelrahman'
age= '21'
country = 'Egypt'

print(f"\"Hello '{name}', How You Doing \\ \"\"\" Your Age Is \"{age}\"\" + And Your Country Is: {country}")

#  **************************************************************************

print(f"\"Hello '{name}', \nHow You Doing \\ \"\"\" Your Age Is \"{age}\"\" +\n And Your Country Is: {country}")


name = 'Elzero'

# Needed Output
print(name[1:2]) # Second Letter Is "l"
print(name[2:3]) # Third Letter Is "z"
print(name[-1]) # Last Letter Is "o"


# Needed Output
print(name[1:4]) # "lze"
print(name[::2]) # "Ezr"
print(name[::-1][1::2]) # "rzE"


name = "#@#@Elzero#@#@"
# Needed Output
print(name.strip("@#")) # Elzero


num = "9"
print(num.zfill(4)) # 0009
num = "15"
print(num.zfill(4)) # 0015
num = "130"
print(num.zfill(4)) # 0130
num = "950"
print(num.zfill(4)) # 0950
num = "1500"
print(num.zfill(4)) # 1500


name_one = "Osama"
name_two = "Osama_Elzero"
print(name_one.zfill(20))
print(name_two.zfill(20))

msg = "I Love Python And Although Love Elzero Web School"

print(msg.count('Love'))

msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "love", 1))

print(msg.replace("<3", "love"))