import os
import json
import cv2
import numpy as np

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

FACES_DIR = os.path.join(BASE_DIR, "data", "faces")
STUDENTS_FILE = os.path.join(BASE_DIR, "data", "students.json")
MODEL_FILE = os.path.join(BASE_DIR, "data", "face_model.yml")
LABELS_FILE = os.path.join(BASE_DIR, "data", "face_labels.json")

recognizer = cv2.face.LBPHFaceRecognizer_create()

with open(STUDENTS_FILE, "r") as file:
    students = json.load(file)

faces = []
labels = []
label_names = {
    int(s["roll_number"]): s["name"] for s in students
}

for student in students:
    roll = student["roll_number"]
    folder = os.path.join(FACES_DIR, roll)

    if not os.path.isdir(folder):
        print("No face samples for:", student["name"])
        continue

    count = 0

    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(folder, filename)
            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

            if image is not None:
                faces.append(image)
                labels.append(int(roll))
                count += 1

    print(student["name"], "-", count, "samples loaded")

if not faces:
    print("No valid face samples found!")
    raise SystemExit

recognizer.train(faces, np.array(labels, dtype=np.int32))
recognizer.save(MODEL_FILE)

with open(LABELS_FILE, "w") as file:
    json.dump(label_names, file)

print("Training completed successfully!")
print("Model saved at:", MODEL_FILE)