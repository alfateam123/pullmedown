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
    try:
        url = sys.argv[1]
        try:
            store_needed = not (sys.argv[2] and sys.argv[2] == '--no-store')
        except IndexError:
            store_needed = True
    except IndexError:
        print ("usage: ./{0} imgur_url [--no-store]".format(sys.argv[0]))
        sys.exit(1)
    rxs = {
        #"^https?://i.imgur.com/([^/]+?)(.png|.jpg|.jpeg).+?": store,
        r"^https?://imgur.com/a/[^/]+?": imguralbum,
        r"^https?://imgur.com/[^/.]+?$": imgursingle}
    for rx in rxs:
        if re.search(rx, url):
        #print ("gotcha!", rx, url)
            album_list = rxs[rx](url, opt_store=store_needed)
            if album_list and not store_needed:
                for image in album_list: print( image )
            break #fulfilled our duty
    else: #in case no "break" has been executed
        print ("the imgur_url is like this: imgur.com/image or imgur.com/a/album.")
