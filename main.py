from PySide import QtGui
import urllib
import sys

import imageSearch

import bacPySide

image = imageSearch.search('zwerg')

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = bacPySide.ControlMainWindow()
    main_window.show()
    sys.exit(app.exec_())


