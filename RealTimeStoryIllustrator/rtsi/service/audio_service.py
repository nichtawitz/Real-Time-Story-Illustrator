import os

from PySide.phonon import Phonon
from gtts import gTTS

import rtsi as img_service


__author__ = 'hoebart'


def speak(window, sentence_list):
    """
    Processes text, generates audio files and plays them.
    :param window: Window which called this function
    :param sentence_list: List of sentences which should be spoken
    """
    media_object = Phonon.MediaObject(window)
    audio_output = Phonon.AudioOutput(Phonon.MusicCategory, window)
    Phonon.createPath(media_object, audio_output)
    media_object.currentSourceChanged.connect(
        window.change_cur_image)  # invoke image change in ui when new sentence starts

    try:
        os.mkdir('temp/')
    except OSError:
        pass

    for i, sentence in enumerate(sentence_list):
        if sentence != "" and sentence != " ":
            window.append_image(img_service.image_from_text(sentence))
            tts = gTTS(text=sentence, lang='de')
            filename = 'temp/temp' + str(i) + '.mp3'
            tts.save(filename)
            media_object.enqueue(Phonon.MediaSource(filename))
            # media_object.play()
    media_object.play()