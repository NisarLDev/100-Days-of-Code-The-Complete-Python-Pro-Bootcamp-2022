# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
#
# Simple Function
#def greet():
# Three print sequence
#  print("First")
#  print("Second")
#  print("Third")
#greet()

# Function that allows for input
# Parameter named "name"
#def greet_with_name(name):
#    print(f"Hello {name}")
#    print(f"How do you do {name}?")
# The current argument for parameter named "name" is "Python"
#greet_with_name("Python")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"You are in {location}")
# Positional arguments
greet_with("Python","Earth")