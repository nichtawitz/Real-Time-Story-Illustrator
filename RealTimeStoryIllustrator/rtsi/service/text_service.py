import random
import re
from multiprocessing.dummy import Pool as ThreadPool
from rtsi.service.audio_service import AudioService

__author__ = 'hoebart'


def derive_keyword(sentence):
    candidates = []
    for word in re.split('\W+', sentence):
        if re.match('[A-Z]', word) is not None:
            candidates.append(word)
    # cap_words.pop(0)  # Remove start of sentence
    if len(candidates) != 0:
        return random.choice(candidates)
    else:
        return None


class TextService:

    def __init__(self, text, window):
        self.sentence_list = re.split('\.|:|;|-|,', text)
        self.window = window

        pool = ThreadPool(4)
        self.keyword_list = pool.map(derive_keyword, self.sentence_list)

        pool.close()
        pool.join()

        self.audio_service = AudioService(window)
        self.audio_service.prepare_voice(self.sentence_list)
        self.audio_service.set_clip_callback(self.window.switch_to_next_image)

        self.image_service = ImageService()

    def start_story(self):
        self.audio_service.start_audio()