import csv
import os
from datetime import datetime

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

ATTENDANCE_FILE = os.path.join(
    BASE_DIR, "data", "attendance.csv"
)


def mark_attendance(roll_number, name):
    today = datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.now().strftime("%H:%M:%S")

    os.makedirs(os.path.dirname(ATTENDANCE_FILE), exist_ok=True)

    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["Roll Number", "Name", "Date", "Time", "Status"]
            )

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if (
                row["Roll Number"] == str(roll_number)
                and row["Date"] == today
            ):
                print(name, "attendance already marked today!")
                return

    with open(ATTENDANCE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            [roll_number, name, today, current_time, "Present"]
        )

    print(name, "attendance marked successfully!")


if __name__ == "__main__":
    mark_attendance("101", "Rahul")