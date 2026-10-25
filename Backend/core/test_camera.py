import cv2
from camera_service import CameraService

camera = CameraService()

if camera.start():
    print("Camera started successfully!")

    while True:
        frame = camera.get_frame()

        if frame is None:
            break

        cv2.imshow("Attendance Camera Test", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.stop()
    cv2.destroyAllWindows()
else:
    print("Camera could not start. Check your webcam.")