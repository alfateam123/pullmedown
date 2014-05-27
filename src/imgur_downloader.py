#!/usr/bin/env python
import requests, re, sys

#(pratically) ripped from https://github.com/nicolapcweek94/empty-mountain/
#I trust this code :D
def store(url, name):
    image_content = requests.get(url)
    with open(name, 'wb') as fd:
        for chunk in image_content.iter_content(1024*(10**6)):
            fd.write(chunk)
    print (url)

def imguralbum(url, opt_store=True):
    html = requests.get(url).text
    names = []
    for s in re.findall(r"<a.+?class=\"zoom\".+?href=\"(.+?)\">", html):
        r = re.search(r"([^/]+?)(.png|.jpg|.jpeg)$", s)
        store("https:" + s, r.group(1) + r.group(2))
        names.append(r.group(1) + r.group(2))
    return names

def imgursingle(url, opt_store=True):
    html = requests.get(url).text
    r = re.search(r"<a.+?href=\".+?/([^/]+?)(.png|.jpg|.jpeg)\">", html)
    if r:
    store(url, r.group(1) + r.group(2))

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
