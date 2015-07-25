import re

from PySide import QtGui, QtCore
from PySide.QtGui import QPixmap

from rtsi.service.text_service import TextService


__author__ = 'hoebart'


class StoryWindow(QtGui.QMainWindow):
    def __init__(self, text):
        """
        Initialize Story Window
        :param text: text that should be displayed
        """
        super().__init__(flags=QtCore.Qt.FramelessWindowHint)
        self.setObjectName("MainWindow")
        self.total_width = self.size().width()
        self.total_height = self.size().height()
        border = self.total_width * 0.1
        spacing = self.total_width * 0.04
        image_width = self.total_width * 0.17
        self.image_list = []
        self.img_index = 0
        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.image_holder = QtGui.QLabel(self.central_widget)
        self.image_holder.setText("")
        self.image_holder.setGeometry(QtCore.QRect(10, 30, 471, 371))
        self.image_holder.setObjectName("image_holder")
        self.image_holder.setAlignment(QtCore.Qt.AlignCenter)

        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("background-color: rgb(50, 50, 50);")

        self.setWindowTitle(
            QtGui.QApplication.translate("StoryWindow", "Real Time Story Teller", None, QtGui.QApplication.UnicodeUTF8))

        self.text_service = TextService(text, self)
        self.text_service.change_img.connect(self.switch_to_next_image)


    def append_images(self, images):
        """
        Adds an image to the 'playlist' of images.
        :param image: Image which should be added
        """
        self.image_list.extend(images)
        self.switch_to_next_image()

    @QtCore.Slot()
    def switch_to_next_image(self):
        """
        Takes next image from the list and displays it e.g. when sentence ends.
        """
        print("Getting signal")
        if self.image_list[self.img_index] is not None:
            img = QPixmap()
            img.loadFromData(self.image_list[self.img_index])
            self.image_holder.setPixmap(img)
            self.central_widget.setLayout(QtGui.QBoxLayout().setAlignment(self.image_holder, QtCore.Qt.AlignHCenter))
            self.central_widget.setLayout(QtGui.QBoxLayout().setAlignment(self.image_holder, QtCore.Qt.AlignVCenter))

        self.img_index += 1
        QtGui.QApplication.processEvents()

    def start(self):
        self.text_service.start_story()
