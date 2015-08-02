from distutils.core import setup
import py2exe

setup(
    windows=["rtsi/main.py"],
    data_files=[("data",[""])]
)