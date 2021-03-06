#!/usr/bin/env python
import click
import re
import os
try:
    from html.parser import HTMLParser
except ImportError:
    from HTMLParser import HTMLParser
from . import main
from . import utils

"""
Downloader for Goodbye to Halos webcomic.
"""

GTH_FIRST_PAGE = "http://www.goodbyetohalos.com/comic/prologue-1"

# py3k compatibility
xrange = range if not ( 'xrange' in dir(__builtins__) ) else xrange

strip_image = lambda text: re.findall('src\="strips\/(\d+\.\w+)"', text)

class GoodbyeToHalosParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.next_url = None
        self.comic_image_url = None

    def gth_reset(self):
        self.next_url = None
        self.comic_image_url = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag.lower() == "a":
            if attrs.get("class", None) == "cc-next":
                self.next_url = attrs["href"]

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        attrs = dict(attrs)
        if tag.lower() == "img":
            if attrs.get("id", None) == "cc-comic":
                self.comic_image_url = attrs["src"]

def save_image(image_url, store_folder):
    if not image_url:
        return

    image_path = os.path.join(store_folder, image_url.split("/")[-1])
    utils.store(image_url, image_path, overwrite=False)

def dump_whole(folder):
    url = None
    parser = GoodbyeToHalosParser()
    next_found = True
    while next_found:
        parser.gth_reset()
        if not url: url = GTH_FIRST_PAGE
        print("downloading ", url)
        text = utils.get_page(url)
        print("parsing ", url)
        parser.feed(text)
        if parser.next_url:
            next_found = True
            url = parser.next_url
        else:
            next_found = False
        print("downloading ", parser.comic_image_url)
        save_image(parser.comic_image_url, folder)

@main.command()
@click.option("--folder", help="specify a folder to store the dump")
@click.argument("action")
def goodbyetohalos(action, folder):
    #parser = argparse.ArgumentParser(description='MegaTokyo downloader')
    #parser.add_argument('action', metavar='action', nargs='?', help='Action (dump)')
    #args = vars(parser.parse_args())

    if action == 'dump':
        utils.create_folder(folder)

        dump_whole(folder)
    else:
        print("the only supported `action` is `dump`")
