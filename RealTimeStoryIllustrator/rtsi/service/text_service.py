import threading
from PySide import QtCore
import random
import re
from multiprocessing.dummy import Pool as ThreadPool
from rtsi.service.audio_service import AudioService
from rtsi.service.image_service import image_from_keyword_list
from threading import  Thread
from time import sleep

__author__ = 'hoebart'


def derive_keyword(sentence):
    # old code:
    '''
    candidates = []
    for word in re.split('\W+', sentence):
        if re.match('[A-Z]', word) is not None:
            candidates.append(word)
    # cap_words.pop(0)  # Remove start of sentence
    if len(candidates) != 0:
        return random.choice(candidates)
    else:
        return None
    '''
    wordlist = [line.rstrip() for line in open('data\dictionary.txt',encoding="utf-8")]

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
    change_img = QtCore.Signal()

    def __init__(self, text, window):
        QtCore.QObject.__init__(self)
        self.word_list = re.split('\s', text)
        self.sentence_list = re.split('\.|:|;|-|,', text)
        self.window = window
        self.keyword_list = []
        self.timing_list = []

        pool = ThreadPool(4)
        self.keyword_list = pool.map(derive_keyword, self.sentence_list)
        pool.close()
        pool.join()
        self.audio_service = AudioService(window)
        audio_thread = threading.Thread(target=self.audio_service.prepare_voice, args=(self.sentence_list,))
        audio_thread.start()
        # self.audio_service.prepare_voice(self.sentence_list)
        # image_list = image_from_keyword_list(self.keyword_list)
        image_thread = threading.Thread(target=image_from_keyword_list, args=(self.keyword_list, window))
        image_thread.start()

    def start_story(self):
        self.audio_service.set_clip_callback(self.window.switch_to_next_image)
        sleep(5)
        self.audio_service.start_audio()
