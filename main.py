import sys 
from PySide6.QtWidgets import QMainWindow, QApplication
from src.ui.mainwindow import Ui_MainWindow as View
from src.logic.task1 import Task1

class MYGUI(QMainWindow, View):
    def __init__(self, parent=None):
        super(MYGUI, self).__init__(parent)
        self.setupUi(self)

        task1 = Task1()
        self.tabWidget.addTab(task1, "Task 1")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MYGUI()
    w.show()
    app.exec()