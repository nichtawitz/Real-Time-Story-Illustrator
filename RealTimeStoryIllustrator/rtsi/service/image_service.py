import json
import logging
import random
import socket
import urllib
import os

from mstranslator import Translator
from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.parse import urlencode

# from multiprocessing.dummy import Pool as ThreadPool
# from PySide.QtGui import QPixmap

__author__ = 'hoebart'
logger = logging.getLogger(__name__)


def request_image(keyword, num_of_try=0, translate=True):
    """
    Queries Google for images and retries up to 5 times if the randomly selected image could not be accessed
    :param keyword:
        string which specifies the image content
    :param num_of_try:
        internal parameter that increases if the selected image could not be retrieved (e.g. Forbidden Error)
    :param translate:
        Should the keyword be translated to english before the search? (may increase result size)
    :return:
        The image data in bytes
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    user_ip = s.getsockname()[0]
    s.close()

    if keyword is None:
        return None
    if translate:
        trans = Translator('__RealTimeStoryIllustrator__','cpXy6YwcqqjO84ncM6jTGMqoey6uPD3N7yoDYbzk8Xk=')
        translatedkw = trans.translate(keyword, lang_from='de', lang_to='en')
    else:
        translatedkw = keyword
    print("Getting image for: " + keyword + " = " + translatedkw)

    if num_of_try > 5:  # no images were found
        logger.error("Could not find an image after 5 tries")
        return None

    term = urllib.parse.quote_plus(translatedkw)

    sites = [line.rstrip() for line in
             open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'sites.txt'),
                  encoding="utf-8")]
    excludedsites = ""
    #for site in sites:
    #    excludedsites = excludedsites + "-site:" + urllib.parse.quote_plus(site) + '%20'


    img_type = '%7Eillustration+AND+clipart'
    url = ('http://ajax.googleapis.com/ajax/services/search/images?' +
           'v=1.0&q=%7E%22' + term + '%22%20' +  img_type + '%20' + excludedsites + '%20&userip=' + user_ip + '&rsz=8&imgsz=medium&safe=active'+ '&tbs=ic:color')
    # print(url)
    response = urlopen(url).read().decode()

    try:
        img_num = random.randint(0, len(json.loads(response)["responseData"]["results"]) - 1)
        #if num_of_try < 4:
        #    if 1+(num_of_try*10) <  random.randint(num_of_try*5, len(json.loads(response)["responseData"]["results"]) - 1):
        #        img_num = random.randint(0, 1+(num_of_try*10))
        #    else:
        #        img_num = random.randint(num_of_try*5, len(json.loads(response)["responseData"]["results"]) - 1)
        #else:
        #    img_num = random.randint(num_of_try*5, len(json.loads(response)["responseData"]["results"]) - 1)
        data = urllib.request.urlopen(json.loads(response)["responseData"]["results"][img_num]["url"]).read()
        return data
    except (HTTPError, TypeError):
        return request_image(keyword, num_of_try + 1, translate=translate)


def image_from_keyword_list(word_list, window):
    """
    Iterates through a keywordlist and requests images for each one.
    :param word_list:
        List of all important keywords
    :param window:
        Story UI that provides the append_image method
    :return:
        The found image or None if the word in the list was None
    """
    for words in word_list:
        if words is None:
            window.append_images([None])
            continue
        temp_list = []
        for word in words:
            temp_list.append(request_image(word, translate=True))

        window.append_images(temp_list)
