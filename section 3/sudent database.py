# The Student Database: 
# Create a list of dictionaries, where each dictionary represents a student with keys: name, 
# grades (a list of integers), and id (a tuple). Calculate the average grade for each student.



# The Student Database
students = [
    {"name": "Alice", "grades": [90, 85, 92], "id": (101, "A")},
    {"name": "Bob", "grades": [75, 80, 70], "id": (102, "B")},
    {"name": "Charlie", "grades": [88, 95, 90], "id": (103, "C")}
]

def average_grade(students_list):
    for student in students_list:
        avg = sum(student["grades"]) / len(student["grades"])

        print(f"{student["name"]}'s average : {avg}")

average_grade(students)