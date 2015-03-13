import os
import random
import re
import shutil
import urllib
from PySide.phonon import Phonon
from gtts import gTTS
from PySide import QtCore, QtGui
from PySide.QtGui import QPixmap, QWidget, QSound, QFrame
import sys
import imageSearch


def close_app():
    """
    Terminates this Application
    """
    delete_temp()
    sys.exit()


def delete_temp():
    """
    delete the temporary sound folder
    """
    shutil.rmtree('temp', ignore_errors=True)


def split_text(text):
    """
    Split text into parts on the characters . : ; -
    :param text: Text to split
    """
    return re.split('\.|:|;|-', text)


def image_from_text(part):
    """
    Find a important word in a sentence and search for a fitting image
    :param part: sentence to analyze
    :return: a suitable image
    """
    cap_words = []
    for word in re.split('\W+', part):
        if re.match('[A-Z]', word) is not None:
            cap_words.append(word)
    cap_words.pop(0)  # Remove first
    if len(cap_words) != 0:
        img = QPixmap()
        word = random.choice(cap_words)
        print(word)
        data = imageSearch.search(urllib.parse.quote_plus(word))
        img.loadFromData(data)
        return img


class MainWindow(QtGui.QMainWindow):
    """Display Tale"""
    def __init__(self, caller, text):
        """
        Initialize Tale Window
        :param caller: calling window
        :param tale: text that should be displayed
        """
        super().__init__(flags=QtCore.Qt.FramelessWindowHint)
        self.setObjectName("MainWindow")
        self.tale = split_text(text)
        self.imageList = []
        self.imageCounter = 0
        self.resize(496, 477)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText("Test")
        self.label.setGeometry(QtCore.QRect(10, 50, 471, 371))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.setCentralWidget(self.centralwidget)
        self.setStyleSheet("background-color: rgb(50, 50, 50);")

        self.setWindowTitle(
            QtGui.QApplication.translate("MainWindow", "Real Time Story Teller", None, QtGui.QApplication.UnicodeUTF8))

        self.get_voice()

    def get_voice(self):
        mediaObject = Phonon.MediaObject(self)
        audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(mediaObject, audioOutput)
        mediaObject.currentSourceChanged.connect(self.change_cur_image)

        try:
            os.mkdir('temp/')
        except OSError:
            pass

        for i, part in enumerate(self.tale):
            if part != "" and part != " ":
                self.imageList.append(image_from_text(part))
                tts = gTTS(text=part, lang='de')
                filename = 'temp/temp' + str(i) + '.mp3'
                tts.save(filename)
                mediaObject.enqueue(Phonon.MediaSource(filename))
                mediaObject.play()
        mediaObject.play()
        mediaObject.finished.connect(delete_temp)

    def change_cur_image(self):
        print(self.imageList)
        if self.imageList[self.imageCounter] is not None:
            print("change cur Image")
            self.label.setPixmap(self.imageList[self.imageCounter])
        self.imageCounter += 1
        QtGui.QApplication.processEvents()


class InitWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main_window = None
        self.setObjectName("Form")
        self.resize(400, 300)
        self.setMinimumSize(QtCore.QSize(400, 300))
        self.verticalLayout = QtGui.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")
        self.centerFrame = QtGui.QFrame(self)
        self.centerFrame.setObjectName("centerFrame")
        self.centerGrid = QtGui.QGridLayout(self.centerFrame)
        self.centerGrid.setContentsMargins(0, 0, 0, 0)
        self.centerGrid.setObjectName("gridLayout_3")
        self.textFrame = QtGui.QFrame(self.centerFrame)
        self.textFrame.setMinimumSize(QtCore.QSize(361, 212))
        self.textFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.textFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.textFrame.setObjectName("textFrame")
        self.textGrid = QtGui.QGridLayout(self.textFrame)
        self.textGrid.setContentsMargins(-1, -1, -1, 5)
        self.textGrid.setObjectName("textGrid")
        self.textEdit = QtGui.QTextEdit(self.textFrame)
        self.textEdit.setTabChangesFocus(True)
        self.textEdit.setObjectName("textEdit")
        self.textGrid.addWidget(self.textEdit, 0, 0, 1, 1)
        self.centerGrid.addWidget(self.textFrame, 1, 0, 1, 1)

        self.finishFrame = QtGui.QFrame(self.centerFrame)
        self.finishFrame.setMinimumSize(QtCore.QSize(0, 35))
        self.finishFrame.setMaximumSize(QtCore.QSize(16777215, 35))
        self.finishFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.finishFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.finishFrame.setObjectName("finishFrame")
        self.finishGrid = QtGui.QGridLayout(self.finishFrame)
        self.finishGrid.setContentsMargins(-1, 0, -1, -1)
        self.finishGrid.setObjectName("finishGrid")

        spacer_item = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.finishGrid.addItem(spacer_item, 0, 0, 1, 1)
        self.finishBtn = QtGui.QPushButton(self.finishFrame)
        self.finishBtn.setMinimumSize(QtCore.QSize(150, 25))
        self.finishBtn.setObjectName("pushButton")
        self.finishGrid.addWidget(self.finishBtn, 0, 1, 1, 1)
        self.centerGrid.addWidget(self.finishFrame, 2, 0, 1, 1)
        self.verticalLayout.addWidget(self.centerFrame)

        QtCore.QMetaObject.connectSlotsByName(self)

        self.finishBtn.clicked.connect(self.open_main_window)

        self.setWindowTitle(QtGui.QApplication.translate("Form", "Märcheneingabe", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setToolTip(QtGui.QApplication.translate("Form", "Es war einmal...", None, QtGui.QApplication.UnicodeUTF8))
        self.finishBtn.setText(QtGui.QApplication.translate("Form", "Erzählung starten...", None, QtGui.QApplication.UnicodeUTF8))

    def open_main_window(self):
        self.main_window = MainWindow(self, self.textEdit.toPlainText())
        self.hide()
        self.main_window.showFullScreen()

