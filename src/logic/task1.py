from PySide6.QtWidgets import QWidget, QLabel, QPushButton
from PySide6.QtCore import Qt
from src.ui.task1 import Ui_Form as View
from src.logic.camera_thread import VideoFrame
from PySide6.QtGui import QImage, QPixmap, QPainter, QColor, QPen

class Task1(QWidget, View):
    def __init__(self, parent=None):
        super(Task1, self).__init__(parent)
        self.setupUi(self)

        self.video_label = self.findChild(QLabel, "video_frame")
        self.screenshot_label = self.findChild(QLabel, "screen_shot")
        
        self.cancel_button = self.findChild(QPushButton, "cancel")
        self.cancel_button.clicked.connect(self.cancel_feed)

        self.start_button = self.findChild(QPushButton, "start")
        self.start_button.clicked.connect(self.start_feed)

        self.camera1 = VideoFrame(0)
        self.camera1.frame_signal.connect(self.imageUpdateSlot)

        self.illegally_sized_1 = 0
        self.illegally_sized_label_1 = self.findChild(QLabel, "Is_label1")
        self.illegally_sized_button_1 = self.findChild(QPushButton, "Is1")
        self.illegally_sized_button_1.clicked.connect(self.increment_illegaly_sized_1)

        self.illegally_sized_2 = 0
        self.illegally_sized_label_2 = self.findChild(QLabel, "Is_label2")
        self.illegally_sized_button_2 = self.findChild(QPushButton, "Is2")
        self.illegally_sized_button_2.clicked.connect(self.increment_illegaly_sized_2)

        self.illegally_sized_3 = 0
        self.illegally_sized_label_3 = self.findChild(QLabel, "Is_label3")
        self.illegally_sized_button_3 = self.findChild(QPushButton, "Is3")
        self.illegally_sized_button_3.clicked.connect(self.increment_illegaly_sized_3)

        self.illegally_sized_4 = 0
        self.illegally_sized_label_4 = self.findChild(QLabel, "Is_label4")
        self.illegally_sized_button_4 = self.findChild(QPushButton, "Is4")
        self.illegally_sized_button_4.clicked.connect(self.increment_illegaly_sized_4)

        
        self.disrupted_nets_1 = 0
        self.disrupted_nets_label_1 = self.findChild(QLabel, "Ds_label1")
        self.disrupted_nets_button_1 = self.findChild(QPushButton, "Ds1")
        self.disrupted_nets_button_1.clicked.connect(self.increment_disrupted_nets_1)

        self.disrupted_nets_2 = 0
        self.disrupted_nets_label_2 = self.findChild(QLabel, "Ds_label2")
        self.disrupted_nets_button_2 = self.findChild(QPushButton, "Ds2")
        self.disrupted_nets_button_2.clicked.connect(self.increment_disrupted_nets_2)

        self.disrupted_nets_3 = 0
        self.disrupted_nets_label_3 = self.findChild(QLabel, "Ds_label3")
        self.disrupted_nets_button_3 = self.findChild(QPushButton, "Ds3")
        self.disrupted_nets_button_3.clicked.connect(self.increment_disrupted_nets_3)

        self.disrupted_nets_4 = 0
        self.disrupted_nets_label_4 = self.findChild(QLabel, "Ds_label4")
        self.disrupted_nets_button_4 = self.findChild(QPushButton, "Ds4")
        self.disrupted_nets_button_4.clicked.connect(self.increment_disrupted_nets_4)


    def imageUpdateSlot(self, image):
        pixmap = QPixmap.fromImage(image)
        self.video_label.setPixmap(pixmap)

    def cancel_feed(self):
        self.camera1.stop()

    def start_feed(self):
        self.camera1.start()

    # def capture_screenshot(self):
    #     camera_pixmap = self.video_label.pixmap()
    #     # Check if camera_pixmap is not None
    #     if camera_pixmap:
    #         screenshot = QPixmap(camera_pixmap.toImage())
    #         self.screenshot_label.setPixmap(screenshot)

    def increment_illegaly_sized_1(self):
        self.illegally_sized_1 += 1
        self.illegally_sized_label_1.setText(f"{self.illegally_sized_1}")    

    def increment_illegaly_sized_2(self):
        self.illegally_sized_2 += 1
        self.illegally_sized_label_2.setText(f"{self.illegally_sized_2}")  

    def increment_illegaly_sized_3(self):
        self.illegally_sized_3 += 1
        self.illegally_sized_label_3.setText(f"{self.illegally_sized_3}")  

    def increment_illegaly_sized_4(self):
        self.illegally_sized_4 += 1
        self.illegally_sized_label_4.setText(f"{self.illegally_sized_4}")  



    def increment_disrupted_nets_1(self):
        self.disrupted_nets_1 +=1
        self.disrupted_nets_label_1.setText(f"{self.disrupted_nets_1}")  

    def increment_disrupted_nets_2(self):
        self.disrupted_nets_2 +=1
        self.disrupted_nets_label_2.setText(f"{self.disrupted_nets_2}")  

    def increment_disrupted_nets_3(self):
        self.disrupted_nets_3 +=1
        self.disrupted_nets_label_3.setText(f"{self.disrupted_nets_3}")  

    def increment_disrupted_nets_4(self):
        self.disrupted_nets_4 +=1
        self.disrupted_nets_label_4.setText(f"{self.disrupted_nets_4}")  

    # def paintEvent(self, event):
    #     painter = QPainter(self)

    #     if self.map_label:
    #         painter.drawImage(self.rect(), self.map_label, self.map_label.rect())    

    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         self.last_point = event.pos()
    #         self.flag = 1

    #     if event.button() == Qt.RightButton:
    #         self.last_point = event.pos()
    #         self.flag = 0

    # def mouseMoveEvent(self, event):
    #     if event.buttons() == Qt.LeftButton and self.flag:
    #         painter = QPainter(self.image)
    #         pen = QPen(QColor('black'), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
    #         painter.setPen(pen)
    #         painter.drawLine(self.last_point, event.pos())
    #         self.last_point = event.pos()
    #         self.update()         

    #     if event.buttons() == Qt.RightButton and not self.flag:
    #         painter = QPainter(self.image)
    #         pen = QPen(QColor('blue'), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
    #         painter.setPen(pen)
    #         painter.drawLine(self.last_point, event.pos())
    #         self.last_point = event.pos()
    #         self.update() 



