import shutil

__author__ = 'hoebart'

import sys

from PySide import QtGui
import rtsi.ui.init_ui as ui


def delete_temp():
    """
    delete the temporary sound folder
    """
    shutil.rmtree('temp', ignore_errors=True)

def delete_egg_info():
    """
    delete the egg-info folder
    """
    shutil.rmtree('*.egg-info', ignore_errors=True)

def main():
    delete_temp()
    #delete_egg_info()
    app = QtGui.QApplication(sys.argv)
    edit_window = ui.InitWindow()
    edit_window.show()
    app.lastWindowClosed.connect(delete_temp)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
