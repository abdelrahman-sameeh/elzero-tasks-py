# Input
# num = 0

# Needed Output
# "Number 0 Is Not Larger Than 0"

# num = input('Enter Number: ').strip()

# num = int(num)
# count = 0

# if(num == 0):
#   print("Number 0 Is Not Larger Than 0")
# else:
#   while True:
#     num-=1
#     if(num==0):
#       break
#     if(num==6):
#       continue
    
#     print(num)
#     count += 1

  
#   print(f'number of count is {count}')

# *****************************************************************************


# Input
# friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]

# Needed Output
# "Mohamed"
# "Shady"
# "Sherif"
# "Friends Printed And Ignored Names Count Is 2"


# counter = 0
# index = -1
# while index < len(friends)-1:
#   index += 1
#   if( (ord(friends[index][0]) >= 97 and ord(friends[index][0]) <=122) ):
#     counter+=1
#   else:
#     print(friends[index])

# print(f"Friends Printed And Ignored Names Count Is {counter}")


# *****************************************************************************

# # Code
# skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

# while skills:
#   # Type The Code Here in One Line
#   print(skills.pop(0))
  
  
# # Needed Output
# "HTML"
# "CSS"
# "JavaScript"
# "PHP"
# "Python"


# *****************************************************************************


# my_friends = []
# max_length = 4


# while(len(my_friends)<max_length):
#   friend = input('Enter Your Friend Name: ').strip()


#   if(friend==friend.capitalize()):
#     my_friends.append(friend)
#     print(f'Your Friend Add Successfully')

#   if(friend == friend.upper()):
#     print('This Name Is Invalid')

#   if(friend == friend.lower()):
#     friend = friend.capitalize()
#     my_friends.append(friend)
#     print(f'First Character To Uppercase, Friend Name Is {friend}')

  
#   print(f'{(max_length-len(my_friends))} Free Space In Friends List')


# *****************************************************************************

# Input
# my_nums = [15, 81, 5, 17, 20, 21, 13]

# # Needed Output
# "1 => 20"
# "2 => 15"
# "3 => 5"
# "All Numbers Printed"

# my_nums.sort(reverse=True)


# for index, num in enumerate(my_nums):
#   print(f'{index} {num}')
# else:
#   print('Loop is finished successfully')
  


# *****************************************************************************

# for i in range(21):
#   if(i==8 or i==6 or i==12):
#     print(str(i))
#   else:
#     print(str(i).zfill(2))

# *****************************************************************************


# Input
# my_ranks = {
#   'Math': 'A',
#   "Science": 'B',
#   'Drawing': 'A',
#   'Sports': 'C'
# }

# percentage = {
#   "A": 100,
#   "B": 80,
#   "C": 40
# }


# # Needed Output
# "My Rank in Math Is A And This Equal 100 Points"
# "My Rank in Science Is B And This Equal 80 Points"
# "My Rank in Drawing Is A And This Equal 100 Points"
# "My Rank in Sports Is C And This Equal 40 Points"
# "Total Points Is 320"

# total = 0
# for rank in my_ranks:
#   print(f"My Rank in Math Is {my_ranks[rank]} And This Equal {percentage[my_ranks[rank]]} Points")
#   total += percentage[my_ranks[rank]]

# print(f"Total Points Is {total}")

# ***************************************************************************


percentage = {
  "A": 100,
  "B": 80,
  "C": 40,
  "D": 20
}

# Input
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

# Needed Output
"------------------------------"
"-- Student Name => Ahmed"
"------------------------------"
"- Math => 100 Points"
"- Science => 20 Points"
"- Draw => 80 Points"
"- Sports => 40 Points"
"- Thinking => 100 Points"
"Total Points For Ahmed Is 340"
"------------------------------"
"-- Student Name => Sayed"
"------------------------------"
"- Math => 80 Points"
"- Science => 80 Points"
"- Draw => 80 Points"
"- Sports => 20 Points"
"- Thinking => 100 Points"
"Total Points For Sayed Is 360"
"------------------------------"
"-- Student Name => Mahmoud"
"------------------------------"
"- Math => 20 Points"
"- Science => 100 Points"
"- Draw => 100 Points"
"- Sports => 80 Points"
"- Thinking => 80 Points"
"Total Points For Mahmoud Is 380"

for student in students:
  print(f'"------------------------------"')
  print(f'"-- Student Name => {student}"')
  print(f'"------------------------------"')
  for subject in students[student]:
    print(f'"- {subject} => {percentage[students[student][subject]]} Points"')