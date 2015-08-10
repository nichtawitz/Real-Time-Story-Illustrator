# Real-Time Story Illustrator

## Project Description

This project should evolve into a desktop story telling prototype. A selected story or fable should 
be "told" by a text to speech engine, additionaly fitting images should be fetched from google image search and finally displayed to the user. The prototype is developed as part of a Bachelor Thesis for Media Informatics at the Vienna University of Technology.

## Architecture

This project will be written mainly in Python, a text to speech library will be integrated with the image query and display code.

![Component Diagram](https://dl.dropboxusercontent.com/s/oy4vh4rdfoao6uf/RTST%20-%20Components.jpg "Component Diagram")

Setup-py is used as build tool for this project. The Text-To-Speech capabilities are provided by the [gTTS](https://github.com/pndurette/gTTS) module. It retrieves spoken text from the Google TTS Engine in Google Translate. To build the User Interface [PySide](http://qt-project.org/wiki/PySide) is used, which provides LGPL-licensed bindings to Qt. As some of the retrived Images from Google could require editing we use [Pillow](http://python-pillow.github.io/) to accomplish this.

## Installing Real-Time Story Illustrator

### Windows:
##### Requirements: 
[Python 3.4](hhttps://www.python.org/downloads/release/python-340/) (or newer) has to be installed on the computer on which Real-Time Story Illustrator will be used. For installation you need to unpack a *.zip, therefore you need software for this. [7-Zip](http://www.7-zip.de/) is an open source software you may use to do this.
##### Note: 
During installation and while running Real-Time Story Illustrator administrator rights may be needed. The reason for the need of administrator rights during installation is that you may need write access to the installation directory. While running Real-Time Story Illustrator the text to speech engine generates a temp-folder with temporary *.mp3 files, therefore administrative access is needed.
##### Installation Process:
* **Step 1**: Download the folder *dist* from our repository on  [github.com](https://github.com/nichtawitz/bac/tree/master). 
* **Step 2**: In *dist* unzip  *RealTimeStoryIllustrator-0.1.zip*. Inside the unzipped files there is a folder named *rtsi* which has to be moved or copy to the destination where the *.bat (*install.bat, start.bat, uninstall.bat*) files are. The folder structure should now look like this:
```
dist
+-- rtsi
|   +-- data
|   +-- service
|   +-- test
|   +-- ui
|   +-- __init__.py
|   +-- main.py
+-- install.bat.
+-- MANIFEST.in
+-- setup.py
+-- start.bat
+-- uninstall.bat
```
* **Step 3**: Double-click install.bat *(Note: If you need administrator rights, right-click on install.bat and click on 'Run as administrator')*. The Batch-file runs ```python setup.py install ``` to install Real-Time Story lllustrator in the site-packages folder of Python with the ```--record installed_files.txt ``` option to keep track where the files are stored *(which is used by uninstall.bat to delete those installed files automatically)*. You may also use ```python setup.py install ``` in the command prompt to install Real-Time Story Illustrator instead of using the Batch-File.

## Starting Real-Time Story Illustrator

To start Real-Time Story Illustrator simply double-click on *start.bat* (Note: If you need administrator rights, right-click on install.bat and click on 'Run as administrator')*. The Batch-file starts the program with the ```start_rtsi``` command. ```start_rtsi``` may also be used in the command prompt to start Real-Time Story Illustrator instead of using the Batch-file.

## Uninstall Real-Time Story Illustrator

Double-click on *uninstall.bat* to uninstall Real-Time Story Illustrator. The Batch-file runs ```python -m pip uninstall RealTimeStoryIllustrator-0.1.zip``` to uninstall the programm and should also delete all files which were generated during installation and are not needed anymore.
