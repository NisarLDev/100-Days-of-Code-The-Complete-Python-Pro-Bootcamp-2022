#Test programme

import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")
# 🚨 Don't change the code above 👆
#Finish of code for the tests

# Split string method
#names_string = input("Give me everybody's names, separated by a comma. ")
#names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Using random module
import random

def selectRandom(names):
 return random.choice(names)
print(selectRandom(names), "is goin to buy the meal today!");

# Using secrets module for secure PRNG
import secrets

def selectRandom(names):
 return secrets.choice(names)
print(selectRandom(names), "is goin to buy the meal today!");

#END OF CODE
#END OF FILE
