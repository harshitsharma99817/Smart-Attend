import cv2
import json
import os

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

STUDENTS_FILE = os.path.join(BASE_DIR, "data", "students.json")

if not os.path.exists(STUDENTS_FILE):
    STUDENTS_FILE = os.path.join(BASE_DIR, "data", "faces", "students.json")
FACES_DIR = os.path.join(BASE_DIR, "data", "faces")

os.makedirs(FACES_DIR, exist_ok=True)

with open(STUDENTS_FILE, "r") as file:
    students = json.load(file)

if not students:
    print("Please register a student first.")
    raise SystemExit

print("Registered students:")
for student in students:
    print(student["roll_number"], "-", student["name"])

roll = input("Enter student's roll number: ").strip()

student = next(
    (s for s in students if s["roll_number"] == roll),
    None
)

if student is None:
    print("Student not found!")
    raise SystemExit

model_path = os.path.join(
    os.path.dirname(__file__),
    "haarcascade_frontalface_default.xml"
)
detector = cv2.CascadeClassifier(model_path)

if detector.empty():
    print("Face detection model not found!")
    raise SystemExit

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Camera could not open!")
    raise SystemExit

student_dir = os.path.join(FACES_DIR, roll)
os.makedirs(student_dir, exist_ok=True)

count = 0
print("Look at the camera. Press Q to stop.")

try:
    while count < 20:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(
            gray, 1.1, 5, minSize=(80, 80)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame, (x, y), (x+w, y+h), (0, 255, 0), 2
            )

            face = gray[y:y+h, x:x+w]
            face = cv2.resize(face, (200, 200))

            path = os.path.join(
                student_dir, f"face_{count + 1}.jpg"
            )
            if cv2.imwrite(path, face):
                count += 1

            break

        cv2.putText(
            frame, f"Samples: {count}/20",
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, (0, 255, 0), 2
        )

        cv2.imshow("Student Face Capture", frame)

        if cv2.waitKey(300) & 0xFF == ord("q"):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()

print(f"Captured {count} face samples for {student['name']}.")