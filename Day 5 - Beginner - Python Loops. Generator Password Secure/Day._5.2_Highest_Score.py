# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

max_value = 0

for num in student_scores:
    if max_value is None or num > max_value:
        max_value = num

print("Maximum value:", max_value)

#Solution on Repl.it: https://replit.com/@NisarLDev/day-5-2-exercise?v=1
#End of code
#End of File