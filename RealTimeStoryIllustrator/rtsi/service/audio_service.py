import os
import re

from PySide.phonon import Phonon
from gtts import gTTS
import time

__author__ = 'hoebartNichtawitz'


def query_tts(sentence_elem, dir_counter):
    """
    Sends a request to a TTS provider and saves the voice files as .mp3
    :param dir_counter: used to create new dirs when restart the program
    :param sentence_elem:
        array with two elements
            0: number of sentence/part
            1: the sentence/part
    :return:
        the filename or None if the sentence/part was empty
    """
    file_counter = sentence_elem[0]
    sentence = sentence_elem[1]
    sentence = re.sub('"','',sentence)

    if sentence != "" and sentence != " ":
        tts = gTTS(text=sentence, lang='de')
        filename = os.path.join(os.path.dirname(__file__), '..',
                                'temp_'+str(dir_counter), 'temp_' + str(file_counter) + '.mp3')
        print("AUDIO SERVICE: Audio file saved under", filename)
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

    def prepare_voice(self, sentence_list, dir_counter):
        """
        Creates the temp folder and puts themin the playlist
        :param dir_counter:
            Is used to determine which new temp order should be generated
            after restarting the application
        :param sentence_list:
            List of all sentences/parts of the story/tale
        """
        try:
            os.mkdir(os.path.join(os.path.dirname(__file__), '..', 'temp_'+str(dir_counter)+'/'))
        except OSError:
            pass

        for idx, sentence in enumerate(sentence_list):
            time.sleep(0.01)
            name = query_tts([idx, sentence], dir_counter)
            self.media_object.enqueue(Phonon.MediaSource(name))

    def start_audio(self):
        """
        Prints the names of the audio files that are playing
        and starts the audio.
        """
        self.media_object.play()

    def set_clip_callback(self, method):
        """
        :param method:
            Gets called when current clip changes
        """
        self.media_object.currentSourceChanged.connect(method)

    def pause_play(self):
        """
        Pauses the story if its playing or resumes the story if its paused
        """
        if self.media_object.state() == Phonon.PausedState:
            self.media_object.play()
        else:
            self.media_object.pause()

    def stop_play(self):
        """
        Stops the story
        """
        self.media_object.pause()
        self.media_object.stop()
        self.media_object.clearQueue()