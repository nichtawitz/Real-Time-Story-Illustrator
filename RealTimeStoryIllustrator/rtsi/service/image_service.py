import json
import logging
import random
import socket
import urllib
from urllib.request import urlopen

from PySide.QtGui import QPixmap

__author__ = 'hoebart'
logger = logging.getLogger(__name__)


def image_from_text(sentence):
        img = QPixmap()

        word = derive_keyword(sentence)
        if word is None:
            return None
        data = request_image(word)

        img.loadFromData(data)
        return img


def request_image(keyword, num_of_try=0):
    if num_of_try > 5:  # no images were found
        logger.error("Could not find an image after 5 tries")
        return

    term = urllib.parse.quote_plus(keyword)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    user_ip = s.getsockname()[0]
    s.close()
    img_type = random.choice(["comic", "clipart", "vector"])
    url = ('http://ajax.googleapis.com/ajax/services/search/images?' +
           'v=1.0&q=' + term + '%20' + img_type + '&userip=' + user_ip + '&rsz=8&imgsz=medium')

    response = urlopen(url).read().decode()
    img_num = random.randint(0, len(json.loads(response)["responseData"]["results"]) - 1)
    try:
        data = urllib.request.urlopen(json.loads(response)["responseData"]["results"][img_num]["url"]).read()
        return data
    except Exception:
        import traceback

        logger.error('generic exception: ' + traceback.format_exc())
        request_image(keyword, num_of_try + 1)