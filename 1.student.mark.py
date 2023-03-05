

#handling students info
num_students = int(input("Enter the number of students : "))
students = []
for i in range(num_students):
    student_id = input("Enter student's ID : ")
    student_name = input("Enter the student's name : ")
    student_dob = input("Enter the student's birthday (DD/MM/YYYY) :")

    students_info = {"id":student_id, "name":student_name, "dob":student_dob}
    students.append(students_info)


#number of courses
num_courses = int(input("Enter the number of courses : "))

courses = []
for i in range(num_courses):
    courses_id = input("Enter course's ID : ")
    courses_name = input("Enter the course's name : ")

    courses_info = {"id":courses_id, "name":courses_name}
    courses.append(courses_info)


#courses selection and student's grading
selected_course = input("Enter the ID of the course you want to input student's marks : ")
for student in students:
    marks = input("Enter marks for student {} in course {}: " .format(student["name"], selected_course))
    student[selected_course] = marks

print("Students:")
for student in students:
    print(student)

print("Courses:")
for course in courses:
    print(course)




