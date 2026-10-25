import json
import os

DATA_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "data"
)
FILE_PATH = os.path.join(DATA_DIR, "students.json")

os.makedirs(DATA_DIR, exist_ok=True)


def register_student(name, roll_number):
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            students = json.load(file)
    else:
        students = []

    for student in students:
        if student["roll_number"] == roll_number:
            print("Roll number already registered!")
            return

    students.append({
        "name": name,
        "roll_number": roll_number
    })

    with open(FILE_PATH, "w") as file:
        json.dump(students, file, indent=4)

    print("Student registered successfully!")


if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")

    register_student(name, roll_number)