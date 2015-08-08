#_._ coding:utf-8 _._
import re
from .utils import get_page, store, pad, UrlNotFoundError
#from collections import namedtuple
from . import main
import click
import logging
logging.basicConfig(level=logging.DEBUG, filename=".pullmedown.log")

from html.parser import HTMLParser

class FakkuParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.fakku_inside_thumbs = False
        self.fakku_images = list()
        self.fakku_twitter_image = ""

    def convert_thumb_url(self, thumb_url):
        #THUMB: //t.fakku.net/images/manga/i/[Taniguchi-san]_Original_Work_-_INSERT_LEVEL_2_Virginity_Thief/thumbs/001.thumb.jpg
        #REAL: //t.fakku.net/images/manga/i/[Taniguchi-san]_Original_Work_-_INSERT_LEVEL_2_Virginity_Thief/images/001.jpg
        #print("got: ", thumb_url)
        real = thumb_url.replace("/thumbs/", "/images/").replace(".thumb.", "")
        #print("real: ", real)
        return real

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        #print("[handle_starttag]", tag, attrs)

        if tag == "meta":
            if "property" in attrs and attrs["property"]=="og:image":
                self.fakku_twitter_image = attrs["content"]
                logging.debug("found meta: {0}".format(self.fakku_twitter_image))
                if self.fakku_twitter_image == "//t.fakku.net/assets/fakku-momoka-thumb.png":
                    self.fakku_twitter_image = ""
                    logging.debug("oh wait, that's the 404 image. sigh.")

        if tag == "div":
            if "id" in attrs and attrs["id"] == "thumbs":
                self.fakku_inside_thumbs = True

        if self.fakku_inside_thumbs:
            if tag == "img" and attrs['class']=="thumb":
                thumb_image = attrs['src']
                real_image  = self.convert_thumb_url(thumb_image)
                logging.debug("found image: {0} -> {1}".format(thumb_image, real_image))
                self.fakku_images.append(real_image)

    def handle_endtag(self, tag):
        if self.fakku_inside_thumbs and tag == "div":
            self.fakku_inside_thumbs = False

def url_by_counter(url, counter):
    number = pad(counter, 3)
    return url.replace("001.jpg", number+".jpg")

def download(doujin_url):
    fp = FakkuParser()
    #print("url: ", doujin_url+"/read")
    read_content = get_page(doujin_url+"/read")
    fp.feed(read_content)
    images = fp.fakku_images
    if images:
        logging.debug("we have images, so we download them directly")
        for image in images:
            store(image, image.split("/")[-1], overwrite=True)
    elif fp.fakku_twitter_image:
        logging.debug("no images, we use the fakku embedded image for twitter as base")
        counter = 1
        full_url = fp.fakku_twitter_image
        try:
            while True:
                image_url = url_by_counter(full_url, counter)
                store(image_url, image_url.split("/")[-1], overwrite=True)
                counter += 1
        except UrlNotFoundError as e:
            pass
    else:
        print("could not find enough information to download the doujin you asked for.")

@main.command()
@click.argument("doujin-url")
def fakku(doujin_url):
    download(doujin_url)
    #raise NotImplementedError("I need two hands to write it, and one is busy right now :^)")
