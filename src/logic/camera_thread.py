from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage, QPixmap
import cv2 as cv

class VideoFrame(QThread):

    frame_signal = Signal(QImage)

    def __init__(self, path):
        super(VideoFrame, self).__init__()
        self.video_path = path

    def run(self):
        self.ThreadActive = True
        capture = cv.VideoCapture(self.video_path)
        while self.ThreadActive:
            ret, frame = capture.read()
            if ret:
                image = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                FilppedImage = cv.flip(image, 1)
                convertToQTformat = QImage(FilppedImage.data, FilppedImage.shape[1], FilppedImage.shape[0], QImage.Format_RGB888)
                
                self.frame_signal.emit(convertToQTformat)

    def stop(self):
        self.ThreadActive = False
        self.quit()            


