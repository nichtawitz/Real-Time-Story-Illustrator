# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initWindow.ui'
#
# Created: Sat Jul 25 14:29:21 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1071, 768)
        Form.setMinimumSize(QtCore.QSize(1024, 768))
        Form.setStyleSheet("background-color: rgb(135, 217, 255);")
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(Form)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame1 = QtGui.QFrame(self.frame)
        self.frame1.setMinimumSize(QtCore.QSize(0, 35))
        self.frame1.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame1.setStyleSheet("background-color: rgb(135, 217, 255);\n"
"background-color: rgb(52, 170, 62);")
        self.frame1.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtGui.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.gridLayout = QtGui.QGridLayout(self.frame1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame1)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame1, 2, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(361, 212))
        self.frame_2.setStyleSheet("background-color: rgb(135, 217, 255);")
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tree_left_corner = QtGui.QLabel(self.frame_2)
        self.tree_left_corner.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tree_left_corner.setText("")
        self.tree_left_corner.setPixmap(QtGui.QPixmap("tree_corner.png"))
        self.tree_left_corner.setScaledContents(True)
        self.tree_left_corner.setObjectName("tree_left_corner")
        self.gridLayout_2.addWidget(self.tree_left_corner, 0, 0, 1, 1)
        self.tree_right = QtGui.QLabel(self.frame_2)
        self.tree_right.setMinimumSize(QtCore.QSize(600, 0))
        self.tree_right.setText("")
        self.tree_right.setPixmap(QtGui.QPixmap("tree_right.png"))
        self.tree_right.setScaledContents(True)
        self.tree_right.setObjectName("tree_right")
        self.gridLayout_2.addWidget(self.tree_right, 0, 1, 1, 1)
        self.tree_left = QtGui.QLabel(self.frame_2)
        self.tree_left.setMinimumSize(QtCore.QSize(150, 400))
        self.tree_left.setText("")
        self.tree_left.setPixmap(QtGui.QPixmap("tree_left.png"))
        self.tree_left.setScaledContents(True)
        self.tree_left.setObjectName("tree_left")
        self.gridLayout_2.addWidget(self.tree_left, 2, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtGui.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 2, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Erzählung starten...", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

