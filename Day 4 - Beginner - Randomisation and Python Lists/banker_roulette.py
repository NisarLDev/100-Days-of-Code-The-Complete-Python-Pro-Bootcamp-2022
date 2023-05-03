#Test programme

import random;
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "));
random.seed(test_seed);

# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ");
names = namesAsCSV.split(", ");
# 🚨 Don't change the code above 👆
#Finish of code for the tests

# Split string method
#names_string = input("Give me everybody's names, separated by a comma. ")
#names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Using random module

# The solution of Angela Yu

# Get the total number of items in list.
num_items = len(names);
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1);
person_who_will_pay = names[random_choice];

print(person_who_will_pay + " is going to buy the meal today!");
##################################################################
##################################################################

# My chosen solution 
import random;

def selectRandom(names):
 return random.choice(names);
print(selectRandom(names), "is going to buy the meal today!");

# Using module of Python "secrets" for secure PRNG
import secrets;

def selectRandom(names):
 return secrets.choice(names);
print(selectRandom(names), "is going to buy the meal today!");

#END OF CODE
#END OF FILE
