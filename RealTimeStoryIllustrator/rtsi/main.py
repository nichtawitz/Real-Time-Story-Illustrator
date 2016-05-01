import os
import shutil
import sys
import glob

from PySide import QtGui, QtCore
import rtsi.ui.main_window as ui


__author__ = 'hoebart'
EXIT_CODE_FOR_REBOOT = -999


def delete_temp():
    """
    delete the temporary sound folder
    """
    for path in glob.glob('temp_*'):
        print("MAIN: Deleting", path)
        shutil.rmtree(os.path.join(os.path.dirname(__file__), path), ignore_errors=True)


def delete_egg_info():
    """
    delete the egg-info folder
    """
    shutil.rmtree('*.egg-info', ignore_errors=True)


def main():
    """
    Main function that starts the application. If the
    EXIT_CODE_FOR_REBOOT is -999 the application is restarted.
    """
    exit_code = 0
    def_counter = 1
    while True:
        delete_temp()
        try:
            app = QtGui.QApplication(sys.argv)
        except RuntimeError:
            app = QtCore.QCoreApplication.instance()
        edit_window = ui.MainWindow(def_counter)
        edit_window.show()
        exit_code = app.exec_()
        if exit_code != EXIT_CODE_FOR_REBOOT:
            break
        def_counter += 1
        print("MAIN: Restart application.")
    return exit_code

if __name__ == "__main__":
    main()
