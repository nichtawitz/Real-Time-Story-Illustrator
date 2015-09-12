# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat Sep 12 21:16:16 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class MainWindow(QtGui.QWidget):

    def __init__(self):
        # Window setup
        self.setObjectName("main_window")
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))

        self.main_layout = QtGui.QGridLayout(self)
        self.main_layout.setSpacing(0)
        self.main_layout.setObjectName("main_layout")

        # Top Frame
        self.image_frame = QtGui.QFrame(self)
        self.image_frame.setObjectName("image_frame")
        self.image_layout = QtGui.QHBoxLayout(self.image_frame)
        self.image_layout.setContentsMargins(5, 5, 5, 5)
        self.image_layout.setObjectName("image_layout")
        # Labels which will hold the 1-3 story images
        self.image1 = QtGui.QLabel(self.image_frame)
        self.image1.setAlignment(QtCore.Qt.AlignCenter)
        self.image1.setObjectName("image1")
        self.image_layout.addWidget(self.image1)
        self.image2 = QtGui.QLabel(self.image_frame)
        self.image2.setAlignment(QtCore.Qt.AlignCenter)
        self.image2.setObjectName("image2")
        self.image_layout.addWidget(self.image2)
        self.image3 = QtGui.QLabel(self.image_frame)
        self.image3.setAlignment(QtCore.Qt.AlignCenter)
        self.image3.setObjectName("image3")
        self.image_layout.addWidget(self.image3)
        self.main_layout.addWidget(self.image_frame, 0, 0, 1, 1)

        # Center Frame
        self.selection_frame = QtGui.QFrame(self)
        self.selection_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.selection_frame.setObjectName("selection_frame")
        self.selection_layout = QtGui.QGridLayout(self.selection_frame)
        self.selection_layout.setHorizontalSpacing(0)
        self.selection_layout.setVerticalSpacing(5)
        self.selection_layout.setObjectName("selection_layout")
        self.combo_box = QtGui.QComboBox(self.selection_frame)
        self.combo_box.setObjectName("combo_box")
        self.selection_layout.addWidget(self.combo_box, 0, 0, 1, 1)
        self.text_edit = QtGui.QTextEdit(self.selection_frame)
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.text_edit.sizePolicy().hasHeightForWidth())
        self.text_edit.setSizePolicy(size_policy)
        self.text_edit.setObjectName("text_edit")
        self.selection_layout.addWidget(self.text_edit, 1, 0, 1, 1)
        self.main_layout.addWidget(self.selection_frame, 1, 0, 1, 1)

        # Bottom Frame
        self.btn_frame = QtGui.QFrame(self)
        self.btn_frame.setMinimumSize(QtCore.QSize(0, 36))
        self.btn_frame.setMaximumSize(QtCore.QSize(16777215, 36))
        self.btn_frame.setObjectName("start_btn_frame")
        self.btn_frame_layout = QtGui.QGridLayout(self.btn_frame)

        self.btn_frame_layout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.btn_frame_layout.setContentsMargins(-1, -1, 12, -1)
        self.btn_frame_layout.setHorizontalSpacing(5)
        self.btn_frame_layout.setVerticalSpacing(0)
        self.btn_frame_layout.setObjectName("start_btn_layout")

        self.status_lbl = QtGui.QLabel(self.btn_frame)
        size_policy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.status_lbl.sizePolicy().hasHeightForWidth())
        self.status_lbl.setSizePolicy(size_policy)
        self.status_lbl.setMinimumSize(QtCore.QSize(0, 23))
        self.status_lbl.setObjectName("status_lbl")
        self.btn_frame_layout.addWidget(self.status_lbl, 0, 0, 1, 1)
        self.start_btn = QtGui.QPushButton(self.btn_frame)
        self.start_btn.setMinimumSize(QtCore.QSize(0, 23))
        self.start_btn.setMaximumSize(QtCore.QSize(16777215, 23))
        self.start_btn.setObjectName("start_btn")
        self.btn_frame_layout.addWidget(self.start_btn, 0, 2, 1, 1)
        self.pause_btn = QtGui.QPushButton(self.btn_frame)
        self.pause_btn.setMinimumSize(QtCore.QSize(0, 23))
        self.pause_btn.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pause_btn.setObjectName("pause_btn")
        self.btn_frame_layout.addWidget(self.pause_btn, 0, 1, 1, 1)
        self.main_layout.addWidget(self.btn_frame, 2, 0, 1, 1)

        self.setWindowTitle(QtGui.QApplication.translate("main_window", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.status_lbl.setText(QtGui.QApplication.translate("main_window", "Status...", None, QtGui.QApplication.UnicodeUTF8))
        self.start_btn.setText(QtGui.QApplication.translate("main_window", "Start Story", None, QtGui.QApplication.UnicodeUTF8))
        self.pause_btn.setText(QtGui.QApplication.translate("main_window", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.image1.setText(QtGui.QApplication.translate("main_window", "Image1", None, QtGui.QApplication.UnicodeUTF8))
        self.image2.setText(QtGui.QApplication.translate("main_window", "Image2", None, QtGui.QApplication.UnicodeUTF8))
        self.image3.setText(QtGui.QApplication.translate("main_window", "Image3", None, QtGui.QApplication.UnicodeUTF8))