import cv2
import json
import os
from attendance import mark_attendance

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

MODEL_FILE = os.path.join(BASE_DIR, "data", "face_model.yml")
LABELS_FILE = os.path.join(BASE_DIR, "data", "face_labels.json")
CASCADE_FILE = os.path.join(
    os.path.dirname(__file__),
    "haarcascade_frontalface_default.xml"
)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(MODEL_FILE)

with open(LABELS_FILE, "r") as file:
    labels = json.load(file)

detector = cv2.CascadeClassifier(CASCADE_FILE)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

marked_this_session = set()

print("Press Q to quit.")

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Camera frame could not be read.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        for (x, y, w, h) in faces:
            face = cv2.resize(
                gray[y:y+h, x:x+w],
                (200, 200)
            )

            label, confidence = recognizer.predict(face)

            if str(label) in labels and confidence < 50:
                name = labels[str(label)]
                text = name
                color = (0, 255, 0)

                if label not in marked_this_session:
                    mark_attendance(str(label), name)
                    marked_this_session.add(label)

            else:
                text = "Unknown"
                color = (0, 0, 255)

            cv2.rectangle(
                frame, (x, y), (x+w, y+h), color, 2
            )

            cv2.putText(
                frame, text, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, color, 2
            )

        cv2.imshow("Face Recognition and Attendance", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()