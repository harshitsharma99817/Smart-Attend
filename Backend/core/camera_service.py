import cv2
import time


class CameraService:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.cap = None
        self.is_running = False

    def start(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(self.camera_id)
            self.is_running = self.cap.isOpened()

        return self.is_running

    def stop(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None

        self.is_running = False

    def get_frame(self):
        if self.is_running and self.cap is not None:
            ret, frame = self.cap.read()

            if ret:
                return frame

        return None