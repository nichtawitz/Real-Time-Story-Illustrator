import os
import shutil
import threading
from PySide import QtCore
import re
from multiprocessing.dummy import Pool as ThreadPool
import regex
from rtsi.service.audio_service import AudioService
from rtsi.service.image_service import image_from_keyword_list
from time import sleep

__author__ = 'hoebart'


def delete_temp():
    """
    delete the temporary sound folder
    """
    print("text_service: Deleting temp folder.")
    shutil.rmtree(os.path.join(os.path.dirname(__file__), 'temp'), ignore_errors=True)


def derive_keyword(sentence):
    """
    Looks for up to 3 interesting and important words in a sentence which will be used to fetch images. Currently uses
    a dictionary based approach (data\dictionary.txt)
    :param sentence:
        The part of the story which should be analyzed
    :return:
        An array with 1 to 3 strings. If no words in the sentence are interesting it returns None
    """
    wordlist = [line.rstrip() for line in
                open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'dictionary.txt'), encoding="utf-8")]

    candidates = []
    for word in re.split('\W+', sentence):
        if word in wordlist:
            candidates.append(word)

    if len(candidates) == 0:
        return None
    else:
        return candidates[0:3]


def start_image_timing(keyword_list, timing_list, change_img):
    for idx, word in enumerate(keyword_list[1:]):
        sleep(timing_list[idx])
        change_img.emit()


class TextService(QtCore.QObject):
    """
    A TextService which handles all text processing including the fetching of images and voice
    """
    change_img = QtCore.Signal()

    def __init__(self, text, window, lang_en, def_counter):
        """
        :param text:
           Complete tale/story
        :param window:
            Story_UI window
        """
        QtCore.QObject.__init__(self)
        self.word_list = re.split('\s', text)
        self.window = window
        self.sentence_list = regex.split("(?V1)(?<=\.|:|;|-|,|\!)", text)
        self.sentence_list = self.join_short_sentences()
        self.keyword_list = []
        self.timing_list = []

        self.pool = ThreadPool(4)
        self.keyword_list = self.pool.map(derive_keyword, self.sentence_list)
        self.pool.close()
        self.pool.join()

        self.audio_service = AudioService(window)
        self.audio_thread = threading.Thread(target=self.audio_service.prepare_voice,
                                             args=(self.sentence_list, def_counter))
        self.audio_thread.setDaemon(True)
        self.audio_thread.start()
        self.image_thread = threading.Thread(target=image_from_keyword_list, args=(self.keyword_list, window, lang_en))
        self.image_thread.setDaemon(True)
        self.image_thread.start()
        # subtitle_thread = threading.Thread(target=window.set_subtitles, args=())
        # subtitle_thread.setDaemon(True)
        # subtitle_thread.start()

    def start_story(self, wait_seconds=5):
        """
        Starts the story telling but waits a few seconds (to preload some data)
        """
        self.audio_service.set_clip_callback(self.window.switch_to_next_image)
        sleep(wait_seconds)
        self.audio_service.start_audio()

    def get_sentence_list(self):
        return self.sentence_list

    def pause_play(self):
        """
        Pauses the audio or ends the Pause
        """
        self.audio_service.pause_play()

    def stop_play(self):
        """
        Stops the Story. Used for restart.
        """
        self.pool.terminate()
        self.audio_service.stop_play()

    def join_short_sentences(self):
        result_list = []
        for sentence in self.sentence_list:
            if len(sentence.split()) > 4:
                result_list.append(sentence)
            else:
                try:
                    result_list[-1] = result_list[-1] + sentence
                except IndexError:
                    result_list.append(sentence)
        return result_list
