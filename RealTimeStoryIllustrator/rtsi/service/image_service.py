import json
import logging
import random
import socket
import urllib
import goslate
from urllib.error import HTTPError
from urllib.request import urlopen
from multiprocessing.dummy import Pool as ThreadPool

from PySide.QtGui import QPixmap

__author__ = 'hoebart'
logger = logging.getLogger(__name__)


def request_image(keyword, num_of_try=0):
    if keyword is None:
        return None
    translatedkw = goslate.Goslate().translate(keyword, 'en')
    print("Getting image for: "+translatedkw)
    if num_of_try > 5:  # no images were found
        logger.error("Could not find an image after 5 tries")
        return

    term = urllib.parse.quote_plus(translatedkw)

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
    except HTTPError:
        import traceback

        logger.error('Image could not be loaded: ' + traceback.format_exc())
        request_image(keyword, num_of_try + 1)


def image_from_keyword_list(word_list):
    pool = ThreadPool(4)

    img_list = pool.map(request_image, word_list)
    pool.close()
    pool.join()

    return img_list
