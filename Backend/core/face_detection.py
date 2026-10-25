import cv2
import os

class FaceDetection:
    def __init__(self):
        model_path = os.path.join(
            os.path.dirname(__file__),
            "haarcascade_frontalface_default.xml"
        )
        self.detector = cv2.CascadeClassifier(model_path)

    def detect_faces(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame, (x, y), (x + w, y + h),
                (0, 255, 0), 2
            )

        return frame, len(faces)