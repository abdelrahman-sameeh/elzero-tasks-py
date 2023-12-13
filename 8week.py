
# def calculate(n1, n2, op='a'):
#   if(op.lower().startswith('a')):
#     return n1+n2
#   elif (op.lower().startswith('s')):
#     return n1-n2
#   elif (op.lower().startswith('m')):
#     return n1*n2


# # Tests
# print(calculate(10, 20)) # 30
# print(calculate(10, 20, "AdD")) # 30
# print(calculate(10, 20, "a")) # 30
# print(calculate(10, 20, "A")) # 30

# print(calculate(10, 20, "S")) # -10
# print(calculate(10, 20, "subTRACT")) # -10

# print(calculate(10, 20, "Multiply")) # 200
# print(calculate(10, 20, "m")) # 200


# ---------------------------------------------------------------------------

# def addition(*nums):
#   result = 0
#   for num in nums:
#     if num==10:
#       continue
#     elif num==5:
#       result+=num
#     else:
#       result+=num
  
#   return result

# # Tests
# print(addition(10, 20, 30, 10, 15)) # 65
# print(addition(10, 20, 30, 10, 15, 5, 100)) # 160


# ---------------------------------------------------------------------------


# def show_skills(name, *skills):
#   print(f'Hello {name} Your Skills Is')
#   for skill in skills:
#     print(f'- {skill}')
# # Input
# show_skills("Osama", "HTML", "CSS", "JS", "Python")

# # Output
# "Hello Osama Your Skills Is"
# "- HTML"
# "- CSS"
# "- JS"
# "- Python"

# ---------------------------------------------------------------------------


# def say_hello(name='Unknown', age='Unknown', country='Unknown'):
#   return f'"Hello {name} Your {age} Is 38 And You Live In {country}"'


# # Input
# print(say_hello("Osama", 38, "Egypt"))

# # Output
# "Hello Osama Your Age Is 38 And You Live In Egypt"


# # Input
# print(say_hello())

# # Output
# "Hello Unknown Your Age Is Unknown And You Live In Unknown"


# ---------------------------------------------------------------------------

# def get_score(**degrees):
#   for key, value in degrees.items():
#     print(f'{key} => {value}')

# # or


# def get_score(**degrees):
#   for item in degrees:
#     print(f'{item} => {degrees[item]}')


# # Tests
# get_score(Math=90, Science=80, Language=70)



# # Output
# "Math => 90"
# "Science => 80"
# "Language => 70"

# ---------------------------------------------------------------------------


def get_people_scores(name='', **scores):
  if(not scores and name):
    print(f"Hello {name} You Have No Scores To Show")
  if (name and scores):
    print(f"Hello {name} This Is Your Score Table:")
    for key, value in scores.items():
      print(f'{key} => {value}')
  if(not name and scores):
    for key, value in scores.items():
      print(f'{key} => {value}')
    
# Test 1
get_people_scores("Osama", Math=90, Science=80, Language=70)

# Output
"Hello Osama This Is Your Score Table:"
"Math => 90"
"Science => 80"
"Language => 70"

# Test 2
get_people_scores("Mahmoud", Logic=70, Problems=60)

# Output
"Hello Mahmoud This Is Your Score Table:"
"Logic => 70"
"Problems => 60"

# Test 3
get_people_scores(Logic=70, Problems=60)

# Output
"Logic => 70"
"Problems => 60"

# Test 4
get_people_scores("Ahmed")

# Output
"Hello Ahmed You Have No Scores To Show"

