import json
import logging
import random
import socket
import urllib
import os
from urllib.error import HTTPError
from urllib.request import urlopen
from urllib.parse import urlencode
from bing_search_api import BingSearchAPI

from mstranslator import Translator

# from multiprocessing.dummy import Pool as ThreadPool
# from PySide.QtG ui import QPixmap

__author__ = 'hoebart'
logger = logging.getLogger(__name__)


def request_image(window, keyword, num_of_try=0, translate=True):
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


    if keyword is None:
        return None
    if translate:
        trans = Translator('__RealTimeStoryIllustrator__','cpXy6YwcqqjO84ncM6jTGMqoey6uPD3N7yoDYbzk8Xk=')
        translatedkw = trans.translate(keyword, lang_from='de', lang_to='en')
    else:
        translatedkw = keyword

    print("Getting image for: " + str(keyword) + " = " + str(translatedkw))

    if num_of_try > 5:  # no images were found
        logger.error("Could not find an image after 5 tries")
        return None

    term = urllib.parse.quote_plus(translatedkw)

    sites = [line.rstrip() for line in
             open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'sites.txt'),
                  encoding="utf-8")]
    excludedsites = ""
    for site in sites:
        excludedsites = excludedsites + "-site:" + urllib.parse.quote_plus(site) + '%20'

    img_type = '%7Eillustration+AND+clipart'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    url = ('http://ajax.googleapis.com/ajax/services/search/images?' +
           'v=1.0&q=' + term + '%20' + img_type + '%20' + excludedsites + '%20&userip=91.141.0.105' +
           '&rsz=8&imgsz=medium&safe=active' + '&tbs=ic:color')

    try:
        params = {'$format': 'json', '$top': 10, 'ImageFilters': '\'Size:Small\''}
        bingKey = open('../bing.key').read()
        api = BingSearchAPI(bingKey)
        result = api.search_image(str(translatedkw),params)
        amount = len(result.json()['d']['results'])
        # print(json.dumps(result.json(), sort_keys=True, indent=2))

        # print(result.json())
        # print(result.json()['d']['results'][0]['MediaUrl'])
        img_num = random.randint(0, amount-1)
        data = urllib.request.urlopen(result.json()['d']['results'][img_num]['MediaUrl'], timeout=2).read()
        return data
    except Exception as e:  # have to catch everything since socket exceptions seem to be broken
        print("trying again, request was denied "+str(e))
        return request_image(window, keyword, num_of_try + 1, translate=translate)


def image_from_keyword_list(word_list, window, english):
    """
    Iterates through a keywordlist and requests images for each one.
    :param word_list:
        List of all important keywords
    :param window:
        Story UI that provides the append_image method
    :param english:
        Boolean if keywords should be translated or not
    :return:
        The found image or None if the word in the list was None
    """
    for words in word_list:
        if words is None:
            window.append_images([None])
            continue
        temp_list = []
        for word in words:
            temp_list.append(request_image(window, word, translate=english))

        window.append_images(temp_list)
