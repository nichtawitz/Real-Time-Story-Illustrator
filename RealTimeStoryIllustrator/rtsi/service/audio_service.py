import os

from PySide.phonon import Phonon
from gtts import gTTS
from multiprocessing.dummy import Pool as ThreadPool
import time

import rtsi.service.image_service as img_service


__author__ = 'hoebart'


def query_tts(sentence_elem):
    """
    Sends a request to a TTS provider and saves the voice files as .mp3
    :param sentence_elem:
        array with two elements
            0: number of sentence/part
            1: the sentence/part
    :return:
        the filename or None if the sentence/part was empty
    """
    file_counter = sentence_elem[0]
    sentence = sentence_elem[1]

    if sentence != "" and sentence != " ":
        tts = gTTS(text=sentence, lang='de')
        filename = os.path.join(os.path.dirname(__file__), '..', 'temp', 'temp' + str(file_counter) + '.mp3')
        tts.save(filename)
        return filename
    else:
        return None


class AudioService:
    """
    Handles audio requests, playing and timing of voice + images
    """
    def __init__(self, window):
        """
        Creates a new AudioService
        :param window:
            QObject of the story ui
        """
        self.media_object = Phonon.MediaObject(window)
        self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory, window)
        Phonon.createPath(self.media_object, self.audio_output)
        self.filename_list = []

    def prepare_voice(self, sentence_list):
        """
        Creates the temp folder and puts themin the playlist
        :param sentence_list:
            List of all sentences/parts of the story/tale
        """
        try:
            os.mkdir(os.path.join(os.path.dirname(__file__), '..', 'temp/'))
        except OSError:
            pass

        for idx, sentence in enumerate(sentence_list):
            time.sleep(0.01)
            name = query_tts([idx, sentence])
            self.media_object.enqueue(Phonon.MediaSource(name))

    def start_audio(self):
        for m in self.media_object.queue():
            print(m.fileName())
        self.media_object.play()

    def set_clip_callback(self, method):
        """
        :param method:
            Gets called when current clip changes
        """
        self.media_object.currentSourceChanged.connect(method)

    def pause_play(self):
        if self.media_object.state() == Phonon.PausedState:
            self.media_object.play()
        else:
            self.media_object.pause()
