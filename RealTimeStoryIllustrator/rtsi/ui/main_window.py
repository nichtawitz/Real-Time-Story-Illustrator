# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Sat Sep 12 21:16:16 2015
# by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

import copy
import os
import queue

from PySide import QtCore, QtGui
from rtsi.service.text_service import TextService

__author__ = 'hoebart_nichtawitz'
EXIT_CODE_FOR_REBOOT = -999


def restart():
    """
    Restarts the application
    """
    # create a signal equivalent to "void someSignal(int, QWidget)"
    return QtCore.QCoreApplication.exit(EXIT_CODE_FOR_REBOOT)


class MainWindow(QtGui.QWidget):

    lang_en = False

    def __init__(self, def_counter):
        super().__init__()
        self.def_counter = def_counter

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
        self.image_holder1 = QtGui.QLabel(self.image_frame)
        self.image_holder1.setAlignment(QtCore.Qt.AlignCenter)
        self.image_holder1.setObjectName("image1")
        self.image_layout.addWidget(self.image_holder1)
        self.image_holder2 = QtGui.QLabel(self.image_frame)
        self.image_holder2.setAlignment(QtCore.Qt.AlignCenter)
        self.image_holder2.setObjectName("image2")
        self.image_layout.addWidget(self.image_holder2)
        self.image_holder3 = QtGui.QLabel(self.image_frame)
        self.image_holder3.setAlignment(QtCore.Qt.AlignCenter)
        self.image_holder3.setObjectName("image3")
        self.image_layout.addWidget(self.image_holder3)
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
        self.start_btn.setEnabled(False)
        self.btn_frame_layout.addWidget(self.start_btn, 0, 2, 1, 1)
        self.pause_btn = QtGui.QPushButton(self.btn_frame)
        self.pause_btn.setMinimumSize(QtCore.QSize(0, 23))
        self.pause_btn.setMaximumSize(QtCore.QSize(16777215, 23))
        self.pause_btn.setObjectName("pause_btn")
        self.pause_btn.setEnabled(False)
        self.btn_frame_layout.addWidget(self.pause_btn, 0, 1, 1, 1)
        self.lang_switch_btn = QtGui.QPushButton(self.btn_frame)
        self.lang_switch_btn.setMinimumSize(QtCore.QSize(0, 23))
        self.lang_switch_btn.setMaximumSize(QtCore.QSize(16777215, 23))
        self.lang_switch_btn.setObjectName("DE")
        self.btn_frame_layout.addWidget(self.lang_switch_btn, 0, 3, 1, 1)
        self.main_layout.addWidget(self.btn_frame, 2, 0, 1, 1)

        self.setWindowTitle(QtGui.QApplication.translate("main_window", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.status_lbl.setText(
            QtGui.QApplication.translate("main_window", "Status...", None, QtGui.QApplication.UnicodeUTF8))
        self.start_btn.setText(
            QtGui.QApplication.translate("main_window", "Start Story", None, QtGui.QApplication.UnicodeUTF8))
        self.pause_btn.setText(
            QtGui.QApplication.translate("main_window", "Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.lang_switch_btn.setText(
            QtGui.QApplication.translate("main_window", "Click to switch Search to EN",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.image_holder1.setText(
            QtGui.QApplication.translate("main_window", "Image1", None, QtGui.QApplication.UnicodeUTF8))
        self.image_holder2.setText(
            QtGui.QApplication.translate("main_window", "Image2", None, QtGui.QApplication.UnicodeUTF8))
        self.image_holder3.setText(
            QtGui.QApplication.translate("main_window", "Image3", None, QtGui.QApplication.UnicodeUTF8))

        # Non GUI members
        self.text_service = None
        self.image_list = queue.Queue()
        self.img_index = 0
        self.sentence_counter = 0
        self.sentence_list = []  # self.text_service.get_sentence_list()
        self.highlighted_sentence_list = []

        # Setup functions & signals/slots
        self.fill_combo_box()
        self.start_btn.clicked.connect(self.start_story)
        self.pause_btn.clicked.connect(self.pause_story)
        self.lang_switch_btn.clicked.connect(self.switch_lan)

        self.combo_box.activated['QString'].connect(self.get_value)
        self.combo_box_index()

    def switch_lan(self):
        """
        Switches the language of the search from German to English or
        from English to German before the application reads a fairytale.
        If the story has started, the button can change the application.
        """
        if self.lang_switch_btn.text() == "Close":
            print("Close button pressed.")
            self.close()
        elif self.lang_en:
            self.lang_switch_btn.setText(
                QtGui.QApplication.translate("main_window", "Click to switch Search to EN", None, QtGui.QApplication.UnicodeUTF8))
            self.lang_en = False
            print("Language Button pressed: Switched to DE.")
        else:
            self.lang_switch_btn.setText(
                QtGui.QApplication.translate("main_window", "Click to switch Search to DE", None, QtGui.QApplication.UnicodeUTF8))
            self.lang_en = True
            print("Language Button pressed: Switched to EN.")

    def start_story(self):
        """
        Is activated with the "Start Story" button. If the story is already
        running or the story is finished, the button changes to the "Restart"
        button to restart application.
        """
        if self.start_btn.text() == "Start Story":
            QtGui.QApplication.processEvents()
            print("Start button pressed")
            # Enable button
            self.pause_btn.setEnabled(False)
            # Disable buttons
            self.lang_switch_btn.setText(
                QtGui.QApplication.translate("main_window", "Close", None, QtGui.QApplication.UnicodeUTF8))
            self.start_btn.setText(
                QtGui.QApplication.translate("main_window", "Close and restart", None, QtGui.QApplication.UnicodeUTF8))
            # Prepare new Story
            self.text_service = None
            self.image_list = queue.Queue()
            self.img_index = 0
            self.sentence_counter = 0
            self.sentence_list = []  # self.text_service.get_sentence_list()
            self.highlighted_sentence_list = []
            # Start story
            self.text_service = TextService(self.text_edit.toPlainText(), self, self.lang_en, self.def_counter)
            self.text_service.change_img.connect(self.switch_to_next_image)
            self.sentence_list = self.text_service.get_sentence_list()
            self.status_lbl.setText("Preloading...")
            QtGui.QApplication.processEvents()
            wait = 0.1
            if len(self.text_service.keyword_list) > 3:
                while self.image_list.qsize() < 2:
                    continue
            else:
                wait = 3
            self.text_service.start_story(wait_seconds=wait)
            self.status_lbl.setText("Story is playing")
            QtGui.QApplication.processEvents()
            # End of Story
        else:
            print("Restart button pressed")
            self.text_service.stop_play()
            self.close()
            restart()

    @QtCore.Slot()
    def switch_to_next_image(self):
        """
        Takes next image from the list and displays it e.g. when sentence ends.
        """
        self.change_highlight()
        try:
            if not self.image_list.empty():
                images = self.image_list.get()
                if len(images) == 1:
                    self.image_holder1.setPixmap(None)

                    img2 = QtGui.QPixmap()
                    img2.loadFromData(images[0])
                    self.image_holder2.setPixmap(img2)

                    self.image_holder3.setPixmap(None)
                elif len(images) == 2:  # center image holder is empty
                    img1 = QtGui.QPixmap()
                    img1.loadFromData(images[1])
                    self.image_holder1.setPixmap(img1)

                    self.image_holder2.setPixmap(None)

                    img2 = QtGui.QPixmap()
                    img2.loadFromData(images[0])
                    self.image_holder3.setPixmap(img2)
                elif len(images) == 3:
                    img1 = QtGui.QPixmap()
                    img1.loadFromData(images[2])
                    self.image_holder1.setPixmap(img1)

                    img2 = QtGui.QPixmap()
                    img2.loadFromData(images[1])
                    self.image_holder2.setPixmap(img2)

                    img3 = QtGui.QPixmap()
                    img3.loadFromData(images[0])
                    self.image_holder3.setPixmap(img3)
        except IndexError:  # gets thrown if one sentence is told
            pass

        self.sentence_counter += 1
        print("TEXT TO SPEACH: Audio file is playing -", self.sentence_counter, "of", len(self.highlighted_sentence_list), "sentence parts.")
        QtGui.QApplication.processEvents()  # Update Gui to reflect changes
        if self.sentence_counter == len(self.highlighted_sentence_list):
            self.end_of_story()

    def combo_box_index(self):
        index = self.combo_box.currentIndex()
        if index < self.combo_box.count() - 1:
            self.combo_box.setCurrentIndex(index + 0)
        else:
            self.combo_box.setCurrentIndex(0)

    def get_value(self):
        """
        Fills the text box with the content of the fairytale and
         enables or disables the "Start story" button.
        """
        if self.combo_box.currentText() == "Choose Fairytale..":
            self.text_edit.setText("")
            self.start_btn.setEnabled(False)
        else:
            self.text_edit.setText(open(os.path.join(os.path.dirname(__file__), '..', 'data', 'fairytales', str(
                self.combo_box.currentText()) + '.txt')).read())
            self.start_btn.setEnabled(True)

    def fill_combo_box(self):
        """
        Fills the combobox with all the stories found in the data.
        """
        tales = []
        path = os.path.join(os.path.dirname(__file__), '..', 'data', 'fairytales')

        for name in os.listdir(path):
            if os.path.isfile(os.path.join(path, name)):
                tales.append(os.path.splitext(name)[0])
        self.combo_box.clear()
        self.combo_box.addItem('Choose Fairytale..')
        self.combo_box.addItems(tales)

        # fairytale = open('data/fairytales/'+str(self.comboBox.currentText())+'.txt')
        # self.textEdit.setText(fairytale.read())

    def append_images(self, images):
        """
        Adds an image to the 'playlist' of images.
        :param image: Image which should be added
        """
        self.image_list.put(images)
        if images != [None]:
            print("IMAGE SERVICE: Image has been put in Queue. Size is now: " + str(self.image_list.qsize()) + ".")
        else:
            print("IMAGE SERVICE: No Image was found in this sentence.")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
        return True

    def pause_story(self):
        """
        Pauses the story and changes the button accordingly.
        """
        print("Pause button pressed")
        self.text_service.pause_play()
        if self.pause_btn.text() == "Pause":
            self.pause_btn.setText("Resume")
            self.status_lbl.setText("Story is paused")
        else:
            self.pause_btn.setText("Pause")
            self.status_lbl.setText("Story is playing")
        QtGui.QApplication.processEvents()

    def change_highlight(self):
        """
        Highlights the spoken parts with bold text.
        """
        self.highlighted_sentence_list = copy.deepcopy(self.sentence_list)
        current_sentence = self.highlighted_sentence_list[self.sentence_counter]
        current_sentence = "<b>" + current_sentence + "</b>"
        self.highlighted_sentence_list[self.sentence_counter] = current_sentence
        # scroll_pos = self.text_edit.horizontalScrollBar().value()
        self.text_edit.setText("".join(self.highlighted_sentence_list))
        # self.text_edit.horizontalScrollBar().setValue
        return

    def end_of_story(self):
        """
        Function for ending the application. Changes buttons and labels.
        """
        self.status_lbl.setText(
            QtGui.QApplication.translate("main_window", "END OF STORY - Restart Application - "
                                                        "Thanks for using Real-Time Story Illustrator",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.pause_btn.setEnabled(False)
        self.pause_btn.setVisible(False)
        self.start_btn.setVisible(True)
        self.start_btn.setEnabled(True)
        self.start_btn.setText(
            QtGui.QApplication.translate("main_window", "Restart", None, QtGui.QApplication.UnicodeUTF8))
        self.lang_switch_btn.setEnabled(True)
        self.lang_switch_btn.setText(
            QtGui.QApplication.translate("main_window", "Close", None, QtGui.QApplication.UnicodeUTF8))