import os

from PySide.phonon import Phonon
from gtts import gTTS
from multiprocessing.dummy import Pool as ThreadPool

import rtsi as img_service


__author__ = 'hoebart'


def query_tts(sentence_elem):
    file_counter = sentence_elem[0]
    sentence = sentence_elem[1]

    if sentence != "" and sentence != " ":
        tts = gTTS(text=sentence, lang='de')
        filename = 'temp/temp' + file_counter + '.mp3'
        tts.save(filename)
        return filename
    else:
        return None


class AudioService:
    def __init__(self, window):
        self.media_object = Phonon.MediaObject(window)
        self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory, window)
        Phonon.createPath(self.media_object, self.audio_output)
        self.filename_list = []

    def prepare_voice(self, sentence_list):
        try:
            os.mkdir('temp/')
        except OSError:
            pass

        pool = ThreadPool(4)
        filename_list = pool.map(query_tts, enumerate(sentence_list))

        for name in filename_list:
            self.media_object.enqueue(Phonon.MediaSource(name))

    def start_audio(self, sentence_index):
        self.media_object.play()

    def set_clip_callback(self, method):
        self.media_object.currentSourceChanged.connect(method)

