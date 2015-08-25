import queue
import re
from time import sleep

from PySide import QtGui, QtCore
from PySide.QtGui import QPixmap

from rtsi.service.text_service import TextService


__author__ = 'hoebart'


class StoryWindow(QtGui.QMainWindow):
    """
    Window that holds all images and is displayed fullscreen
    """
    def __init__(self, text):
        """
        Initialize Story Window
        :param text: text that should be displayed
        """
        super().__init__(flags=QtCore.Qt.FramelessWindowHint)
        self.setObjectName("MainWindow")

        self.image_list = queue.Queue()
        self.img_index = 0
        self.setStyleSheet("background-color: rgb(50, 50, 50);")

        self.central_widget = QtGui.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.main_layout = QtGui.QVBoxLayout(self.central_widget)
        self.main_layout.setObjectName("mainlayout")
        spacer_item = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.main_layout.addItem(spacer_item)
        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.grid_layout.setObjectName("grid_layout")

        self.image_frame = QtGui.QFrame(self)
        self.image_frame.setMinimumSize(QtCore.QSize(0, 400))
        self.image_frame.setMaximumSize(QtCore.QSize(16777215, 512))

        self.image_layout = QtGui.QHBoxLayout(self.image_frame)
        self.image_layout.setSpacing(120)
        self.image_layout.setContentsMargins(40, -1, 40, -1)

        self.image_holder3 = QtGui.QLabel(self.image_frame)
        self.image_holder3.setAlignment(QtCore.Qt.AlignCenter)
        self.image_layout.addWidget(self.image_holder3)

        self.image_holder2 = QtGui.QLabel(self.image_frame)
        self.image_holder2.setAlignment(QtCore.Qt.AlignCenter)
        self.image_layout.addWidget(self.image_holder2)

        self.image_holder1 = QtGui.QLabel(self.image_frame)
        self.image_holder1.setAlignment(QtCore.Qt.AlignCenter)
        self.image_layout.addWidget(self.image_holder1)

        self.grid_layout.addWidget(self.image_frame, 0, 0, 1, 1)
        self.main_layout.addLayout(self.grid_layout)

        self.frame = QtGui.QFrame(self)
        self.frame.setMinimumSize(QtCore.QSize(0, 100))

        self.subtitle_layout = QtGui.QGridLayout(self.frame)

        self.subtitle_label = QtGui.QLabel(self.frame)
        self.subtitle_label.setAlignment(QtCore.Qt.AlignCenter)
        self.subtitle_label.setObjectName("subtitle_label")

        self.subtitle_layout.addWidget(self.subtitle_label, 0, 0, 1, 1)
        self.main_layout.addWidget(self.frame)
        self.setCentralWidget(self.central_widget)

        self.subtitle_label.setStyleSheet("font: bold 22px; color: white;")
        self.subtitle_label.setText(QtGui.QApplication.translate("Form", "Subtitles", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowTitle(
            QtGui.QApplication.translate("StoryWindow", "Real Time Story Teller", None, QtGui.QApplication.UnicodeUTF8))

        self.text_service = TextService(text, self)
        self.sentence_counter = 0
        self.sentence_list = self.text_service.get_sentence_list()
        self.text_service.change_img.connect(self.switch_to_next_image)

    def append_images(self, images):
        """
        Adds an image to the 'playlist' of images.
        :param image: Image which should be added
        """
        self.image_list.put(images)
        print("Image has been put in Queue size is now:"+str(self.image_list.qsize()))

    @QtCore.Slot()
    def switch_to_next_image(self):
        """
        Takes next image from the list and displays it e.g. when sentence ends.
        """
        self.change_subtitles()
        temptext = ""
        try:
            if not self.image_list.empty():
                images = self.image_list.get()
                img1 = QPixmap()
                if len(images) == 1:
                    self.image_holder1.setPixmap(None)

                    img2 = QPixmap()
                    img2.loadFromData(images[0])
                    self.image_holder2.setPixmap(img2)

                    self.image_holder3.setPixmap(None)
                elif len(images) == 2:
                    img1 = QPixmap()
                    img1.loadFromData(images[1])
                    self.image_holder1.setPixmap(img1)

                    self.image_holder2.setPixmap(None)

                    img2 = QPixmap()
                    img2.loadFromData(images[0])
                    self.image_holder3.setPixmap(img2)
                elif len(images) == 3:
                    img1 = QPixmap()
                    img1.loadFromData(images[2])
                    self.image_holder1.setPixmap(img1)

                    img2 = QPixmap()
                    img2.loadFromData(images[1])
                    self.image_holder2.setPixmap(img2)

                    img3 = QPixmap()
                    img3.loadFromData(images[0])
                    self.image_holder3.setPixmap(img3)
        except IndexError:  # gets thrown if one sentence is told
            pass

        QtGui.QApplication.processEvents()

    def change_subtitles(self):
        self.subtitle_label.setText(self.sentence_list[self.sentence_counter])
        print(self.sentence_list[self.sentence_counter])
        self.sentence_counter += 1

    def start(self):
        self.text_service.start_story(wait_seconds=5)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Space:
            self.text_service.pause_play()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.close()
        return True

