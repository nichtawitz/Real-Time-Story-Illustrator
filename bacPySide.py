# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bac.ui'
#
# Created: Sat Dec  6 16:36:21 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
import urllib

from PySide import QtCore, QtGui
from PySide.QtGui import QPixmap
import imageSearch


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 477)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 471, 371))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 281, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("Hexe")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 10, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.refreshsearch)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Real Time Story Teller", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Search Image", None, QtGui.QApplication.UnicodeUTF8))

    def refreshsearch(self):
        self.label.setText("Searching new Image...")
        QtGui.QApplication.processEvents()
        term = urllib.parse.quote_plus(self.lineEdit.text())
        path = imageSearch.search(term)
        data = urllib.request.urlopen(path).read()
        img = QPixmap()
        img.loadFromData(data)
        self.label.setPixmap(img)
        QtGui.QApplication.processEvents()

class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)