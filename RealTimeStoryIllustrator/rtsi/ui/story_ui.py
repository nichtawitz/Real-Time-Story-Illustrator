import re

from PySide import QtGui, QtCore

import rtsi.service.audio_service as audio

__author__ = 'hoebart'


class StoryWindow(QtGui.QMainWindow):
    def __init__(self, text):
        """
        Initialize Story Window
        :param text: text that should be displayed
        """
        super().__init__(flags=QtCore.Qt.FramelessWindowHint)
        self.setObjectName("MainWindow")
        sentence_list = re.split('\.|:|;|-', text)  # Split input Text in parts/sentences
        self.image_list = []
        self.img_index = 0
        self.resize(496, 477)
        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.label = QtGui.QLabel(self.central_widget)
        self.label.setText("Test")
        self.label.setGeometry(QtCore.QRect(10, 50, 471, 371))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.setCentralWidget(self.central_widget)
        self.setStyleSheet("background-color: rgb(50, 50, 50);")

        self.setWindowTitle(
            QtGui.QApplication.translate("StoryWindow", "Real Time Story Teller", None, QtGui.QApplication.UnicodeUTF8))

        audio.speak(self, sentence_list)

    def append_image(self, image):
        """
        Adds an image to the 'playlist' of images.
        :param image: Image which should be added
        """
        self.image_list.append(image)

    def change_cur_image(self):
        """
        Takes next image from the list and displays it e.g. when sentence ends.
        """
        if self.image_list[self.img_index] is not None:
            print("change cur Image")
            self.label.setPixmap(self.image_list[self.img_index])
        self.img_index += 1
        QtGui.QApplication.processEvents()