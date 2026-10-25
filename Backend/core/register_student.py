import json
import os

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

STUDENTS_FILE = os.path.join(BASE_DIR, "data", "students.json")

os.makedirs(os.path.dirname(STUDENTS_FILE), exist_ok=True)

if os.path.exists(STUDENTS_FILE):
    with open(STUDENTS_FILE, "r") as file:
        students = json.load(file)
else:
    students = []

roll = input("Enter roll number: ").strip()
name = input("Enter student name: ").strip()

if not roll or not name:
    print("Roll number and name cannot be empty!")

elif any(s["roll_number"] == roll for s in students):
    print("This roll number is already registered!")

else:
    students.append({
        "roll_number": roll,
        "name": name
    })

    with open(STUDENTS_FILE, "w") as file:
        json.dump(students, file, indent=4)

    print("Student registered successfully!")
    print("Now capture face samples and retrain the model.")