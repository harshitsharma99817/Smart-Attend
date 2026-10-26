from flask import Flask, request
from flask_cors import CORS
import json
import csv
import os

app = Flask(__name__)
CORS(app)

# Project root folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(BASE_DIR, "data")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.json")
ATTENDANCE_FILE = os.path.join(DATA_DIR, "attendance.csv")


def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []

    with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def home():
    return {"message": "SmartAttend Backend is running!"}


@app.route("/api/students", methods=["GET"])
def get_students():
    return load_students()


@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True) or {}

    name = str(data.get("name", "")).strip()
    roll_number = str(data.get("roll_number", "")).strip()

    if not name or not roll_number:
        return {"error": "Name and roll number are required"}, 400

    students = load_students()

    if any(str(s.get("roll_number")) == roll_number for s in students):
        return {"error": "Roll number already exists"}, 409

    students.append({
        "roll_number": roll_number,
        "name": name
    })

    os.makedirs(DATA_DIR, exist_ok=True)

    with open(STUDENTS_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    return {
        "message": "Student added successfully",
        "student": students[-1]
    }, 201


@app.route("/api/attendance", methods=["GET"])
def get_attendance():
    records = []

    if not os.path.exists(ATTENDANCE_FILE):
        return records

    with open(ATTENDANCE_FILE, "r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append({
                "roll_number": row.get("Roll Number", ""),
                "name": row.get("Name", ""),
                "date": row.get("Date", ""),
                "time": row.get("Time", ""),
                "status": row.get("Status", "")
            })

    return records


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)