Real Time Story Telling
=======================

Project Description
-------------------

This project should evolve into a desktop story telling prototype. A selected story or fable should 
be "told" by a text to speech engine, additionaly fitting images should be fetched from google image search and finally displayed to the user. The prototype is developed as part of a Bachelor Thesis for Media Informatics at the Vienna University of Technology.

Architecture
------------
This project will be written mainly in Python, a text to speech library will be integrated with the image query and display code.

![Component Diagram](https://dl.dropboxusercontent.com/s/oy4vh4rdfoao6uf/RTST%20-%20Components.jpg "Component Diagram")

Setup-py is used as build tool for this project. The Text-To-Speech capabilities are provided by the [gTTS](https://github.com/pndurette/gTTS) module. It retrieves spoken text from the Google TTS Engine in Google Translate. To build the User Interface [PySide](http://qt-project.org/wiki/PySide) is used, which provides LGPL-licensed bindings to Qt. As some of the retrived Images from Google could require editing we use [Pillow](http://python-pillow.github.io/) to accomplish this.
