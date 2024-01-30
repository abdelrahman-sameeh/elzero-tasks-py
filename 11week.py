
# tasks from 76 to 78


# need output
# "Random Number Between 10 And 50 =>" "Show The Random Number Here"
# "Random Even Number Between 2 And 10 =>" "Show The Random Even Number Here"
# "Random Odd Number Between 1 And 9 =>" "Show The Random Odd Number Here"

# Module Methods Content Here

import random

# def get_event_random_number(n1, n2):
  


print(f"Random Number Between 10 And 50 => {random.randrange(10, 50)} ")
print(f"Random Even Number Between 2 And 10 => {random.randrange(2, 10, 2)} ")
print(f"Random Odd Number Between 1 And 9 => {random.randrange(1, 9, 2)} ")


print('*'*50)

# -------------------------------------------------------------------------------

import my_mod

print(my_mod.say_hello('Abdelrahman'))
print(my_mod.say_welcome('Abdelrahman'))




print('*'*50)

# -------------------------------------------------------------------------------

from my_mod import say_welcome

print(say_welcome('Abdelrahman'))




print('*'*50)



# -------------------------------------------------------------------------------


# tasks from-79-to-80



# The Date Is "2021, 6, 25"
# Today Is "2021, 8, 10"

# Message Will Be
# "Days From 2021-06-25 To 2021-08-10 Is => 46"


from datetime import datetime

start_date = datetime(2021, 6, 25)
end_date = datetime(2024, 1, 30)

print(f"Days From {start_date.date()} To {end_date.date()} Is => {(end_date.date()-start_date.date()).days}")



print('*'*50)

# -------------------------------------------------------------------------------

from datetime import datetime

# Today Is "2021, 8, 10"

# "2021-08-10"
# "Aug 10, 2021"
# "10 - Aug - 2021"
# "10 / Aug / 21"
# "10 / August / 2021"
# "Tue, 10 August 2021"

print(datetime.now().strftime(f"%Y-%m-%d"))
print(datetime.now().strftime(f"%b %d, %Y"))
print(datetime.now().strftime(f"%d - %b - %Y"))
print(datetime.now().strftime(f"%d / %b / %y"))
print(datetime.now().strftime(f"%d / %B / %Y"))
print(datetime.now().strftime(f"%a %d %B %Y"))


# for date "30-1-2024"
# بالنسبه للتاريخ
# %Y => 2024
# %y => 24
# %b => Jan
# %B => January
# %d => 10
# %D => 01/30/24
# %a => Tue
# %m => 01   الشهر بالرقم



print('*'*50)

# -------------------------------------------------------------------------------

# tasks from-81-to-85

def reverse_string(my_string):
  for char in my_string[::-1]:
    yield char

# Reverse The String
for c in reverse_string("Elzero"):
  print(c)


print('*'*50)

# -------------------------------------------------------------------------------


# Create Your Decorator Here

def my_decorator(fn):
  def nested():
    print('Sugar Added From Decorators')
    fn()
    print('#'*20)
  return nested

@my_decorator
def make_tea():
  print("Tea Created")

@my_decorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()


# Needed Output

# "Sugar Added From Decorators"
# "Tea Created"
# "####################"
# "Sugar Added From Decorators"
# "Coffe Created"
# "####################"



print('*'*50)

# -------------------------------------------------------------------------------


# create a decorator to pass name if function and print it in main function

def my_decorator(name):
  def decorator(fn):
    def nested():
      fn(name)
    return nested
  return decorator


@my_decorator("abdelrahman")
def say_hello(name):
  print(f'hello {name}')


say_hello()


