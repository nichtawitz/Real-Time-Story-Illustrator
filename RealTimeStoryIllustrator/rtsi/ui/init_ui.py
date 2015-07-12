from PySide.QtGui import QWidget

from rtsi.ui.story_ui import *


__author__ = 'hoebart'


class InitWindow(QWidget):
    """
    Window where story is chosen or defined
    """
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

        self.finishBtn.clicked.connect(self.open_story_window)

        self.setWindowTitle(
            QtGui.QApplication.translate("Form", "Märcheneingabe", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setToolTip(
            QtGui.QApplication.translate("Form", "Es war einmal...", None, QtGui.QApplication.UnicodeUTF8))
        self.finishBtn.setText(
            QtGui.QApplication.translate("Form", "Erzählung starten...", None, QtGui.QApplication.UnicodeUTF8))

    def open_story_window(self):
        self.main_window = StoryWindow(self.textEdit.toPlainText())
        self.hide()
        self.main_window.showFullScreen()
