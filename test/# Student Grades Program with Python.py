# Student Grades Program with Python

# Function to print all students and their scores
students = []

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    name = input(f"Enter student {i+1} name: ")
    score = int(input(f"Enter {name}'s score: "))

    students.append((name, score))

average = 0
Top_Score = 0
Failing_Students = []
for student, score in students:
    average += score
    print("All students and scores:") 
    print(f"{student} - {score}")
    if score < 60:
        Failing_Students.append(student)
    if score > Top_Score:
        Top_Score = score
        top_student = student
print(f"Average: {average/num_students}")
print(f"Top_Student: {top_student} ({Top_Score})")
print(f"Failing_Student: {",".join(Failing_Students)}")