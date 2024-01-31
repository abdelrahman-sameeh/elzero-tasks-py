"""
  this is my pylint module
"""
my_friends = ["Ahmed", "Osama", "Sayed"]

def say_hello(some_people) -> list:
    """
    this is a doc string for this function
    """
    for someone in some_people:
        print(f"Hello {someone}")

say_hello(my_friends)

