# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? " + " If you put it in the right number, you win the treasure. " )
# 🚨 Don't change the code above 👆
horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal -1] = "X"

if position == "23":
  print(" Congratulations, you've won the treasure.")
else:
  print("Sorry. "+"Try again.")
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
#END OF CODE
#END OF FILE
