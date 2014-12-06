__author__ = 'konstantin'

import json
from urllib.request import *
import socket
import random


def search(term):
    """
    Requests images for the term from Google
    one gets selected at random and returned
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    user_ip = s.getsockname()[0]
    s.close()
    itype = random.choice(["comic", "clipart", "vector"])
    url = ('http://ajax.googleapis.com/ajax/services/search/images?' +
           'v=1.0&q=' + term + '%20' + itype + '&userip=' + user_ip + '&rsz=8&imgsz=large')

    response = urlopen(url).read().decode()
    img_num = random.randint(0, len(json.loads(response)["responseData"]["results"])-1)
    return json.loads(response)["responseData"]["results"][img_num]["url"]


