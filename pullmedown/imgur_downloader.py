#!/usr/bin/env python
import click
from . import main
from . import utils
import re
import sys
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

try:
    from html.parser import HTMLParser
except ImportError:
    log.debug("could not import HTMLParser from html.parser, pullmedown is running under py2")
    from HTMLParser import HTMLParser

class ImgurParser(HTMLParser):
    def __init__(self, is_album=True):
        HTMLParser.__init__(self)
        self.imguralbum_urls = list()
        self.imgur_isalbum = is_album

    def imgur_istagvalid(self, attrs):
        if self.imgur_isalbum:
            return attrs.get("target", None) == "_blank" and attrs.get("href", "").startswith("//i.imgur")
        else:
            return attrs.get("class", None) == "zoom" and attrs.get("href", "").startswith("//i.imgur")

    def handle_starttag(self, tag, attrs):
        #the only use case for a [(key, value)] thing is unit testing a templating engine. but that's not the case...
        attrs = dict(attrs)
        if tag == "a":
            log.debug("found an 'a' tag, attrs are: {}".format(attrs))
            #if attrs.get("class", "") == "class" and "data-reactid" in attrs:
            if self.imgur_istagvalid(attrs): #attrs.get('target', None) == '_blank' and attrs.get("href", "").startswith('//i.imgur'):
                self.imguralbum_urls.append("http:"+attrs["href"])

def imguralbum(url, opt_store=True):
    log.debug("called imguralbum: url {}, opt_store {}".format(url, opt_store))
    html = utils.get_page(url)
    assert html, "could not retrieve the html page."
    #for s in re.findall(r"<a.+?class=\"zoom\".+?href=\"(.+?)\">", html):
    #    r = re.search(r"([^/]+?)(.png|.jpg|.jpeg)$", s)
    #    if opt_store:
    #        utils.store("https:" + s, r.group(1) + r.group(2))
    #    names.append(r.group(1) + r.group(2))
    parser = ImgurParser()
    parser.feed(html)
    urls = parser.imguralbum_urls
    log.debug("retrieved some images: {}".format(urls))
    if opt_store:
        for url in urls: utils.store(url, url.split("/")[-1])
    return urls

def imgursingle(url, opt_store=True):
    html = utils.get_page(url)
    #r = re.search(r"<a.+?href=\"(.+?/([^/]+?)(.png|.jpg|.jpeg))\">", html)
    parser = ImgurParser(is_album=False)
    parser.feed(html)
    if parser.imguralbum_urls:
        #print (r.group(1), r.group(2)+r.group(3))
        #utils.store("http:"+r.group(1), r.group(2) + r.group(3))
        utils.store(parser.imguralbum_urls[-1], parser.imguralbum_urls[-1].split("/")[-1])

#if __name__ == "__main__":
@main.command()
@click.argument("imgur_url")
@click.option("--no_store", default=False)
def imgur(imgur_url, no_store):
    url, store_needed = imgur_url, (not no_store)
    rxs = {
        #"^https?://i.imgur.com/([^/]+?)(.png|.jpg|.jpeg).+?": store,
        r"^https?://imgur.com/a/[^/]+?": imguralbum,
        r"^https?://imgur.com/[^/.]+?$": imgursingle}
    for rx in rxs:
        if re.search(rx, url):
            logging.info("url is {}, executing the function related to the regex {}".format(url, rx))
            album_list = rxs[rx](url, opt_store=store_needed)
            if album_list : #and not store_needed:
                for image in album_list: print( image )
            break #fulfilled our duty
    else: #in case no "break" has been executed
        print ("the imgur_url is like this: https://imgur.com/<image> or https://imgur.com/a/<album>.")
        sys.exit(1)
