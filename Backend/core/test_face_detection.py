print("TEST FILE STARTED")

import cv2
from camera_service import CameraService
from face_detection import FaceDetection

print("Imports successful!")

camera = CameraService()
face_detector = FaceDetection()

print("Camera and detector created!")

if not camera.start():
    print("Camera could not open!")
    exit()

print("Camera opened successfully!")

while True:
    frame = camera.get_frame()

    if frame is None:
        print("Frame not received!")
        break

    frame, count = face_detector.detect_faces(frame)
    cv2.putText(
        frame, f"Faces Detected: {count}",
        (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
        0.8, (0, 255, 0), 2
    )

    cv2.imshow("Skillwallet Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.stop()
cv2.destroyAllWindows()