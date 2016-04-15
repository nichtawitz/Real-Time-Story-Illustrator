import os
import shutil
import sys

from PySide import QtGui
import rtsi.ui.main_window as ui


__author__ = 'hoebart'


def delete_temp():
    """
    delete the temporary sound folder
    """
    shutil.rmtree(os.path.join(os.path.dirname(__file__), 'temp'), ignore_errors=True)


def delete_egg_info():
    """
    delete the egg-info folder
    """
    shutil.rmtree('*.egg-info', ignore_errors=True)


def main():
    delete_temp()
    # delete_egg_info()
    app = QtGui.QApplication(sys.argv)
    edit_window = ui.MainWindow()
    edit_window.show()
    app.lastWindowClosed.connect(delete_temp)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
