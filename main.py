# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

tHeight = 0

for height in student_heights:
    tHeight += height
print(f"Total combined height = {tHeight}")

numStudents = 0

for student in student_heights:
    numStudents += 1
print(f"Total number of students = {numStudents}")

avgHeight = round(tHeight / numStudents)
print(f"Combined averaged height = {avgHeight}")
