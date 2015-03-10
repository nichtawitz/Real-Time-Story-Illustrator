from PySide import QtGui
import urllib
import sys

import imageSearch

import GUI


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    edit_window = GUI.InitWindow()
    edit_window.show()
    sys.exit(app.exec_())


