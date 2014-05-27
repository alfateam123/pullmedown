#!/usr/bin/env python
import utils
import re
import sys

def imguralbum(url, opt_store=True):
    html = utils.get_page(url)
    names = []
    for s in re.findall(r"<a.+?class=\"zoom\".+?href=\"(.+?)\">", html):
        r = re.search(r"([^/]+?)(.png|.jpg|.jpeg)$", s)
        if opt_store: utils.store("https:" + s, r.group(1) + r.group(2))
        names.append(r.group(1) + r.group(2))
    return names

def imgursingle(url, opt_store=True):
    html = utils.get_page(url)
    r = re.search(r"<a.+?href=\"(.+?/([^/]+?)(.png|.jpg|.jpeg))\">", html)
    if r:
        #print (r.group(1), r.group(2)+r.group(3))
        utils.store("http:"+r.group(1), r.group(2) + r.group(3))

if __name__ == "__main__":
    url = sys.argv[1]
    rxs = {
        #"^https?://i.imgur.com/([^/]+?)(.png|.jpg|.jpeg).+?": store,
        r"^https?://imgur.com/a/[^/]+?": imguralbum,
        r"^https?://imgur.com/[^/.]+?$": imgursingle}
    for rx in rxs:
        if re.search(rx, url):
        #print ("gotcha!", rx, url)
            rxs[rx](url)
