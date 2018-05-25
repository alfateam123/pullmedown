#!/usr/bin/env python
import re
from . import utils
from . import main 
import click
import os

"""
Downloader for MegaTokyo webcomic.
"""

# py3k compatibility
xrange = range if not ( 'xrange' in dir(__builtins__) ) else xrange

strip_image = lambda text: re.findall('src\="strips\/(\d+\.\w+)"', text)

def last_comic(download=True, return_number=False):
    text = utils.get_page('http://megatokyo.com')
    #print (strip_image(text))
    strip_number = int(strip_image(text)[0][:-4]) #removing .png || .gif
    if download:
        dump_single(strip_number, image_format=strip_image(text)[0][-4:])
    if return_number:
        return strip_number

def dump_single(number, image_format=None, folder="."):
    if not image_format:
        text = utils.get_page('http://megatokyo.com/strip/{0}'.format(number)) #retrieving the image format
        #print (strip_image(text))
        strip_name = strip_image(text)[0]
    else:
        strip_name = str(number)+image_format
    store_path = os.path.join(folder, strip_name)
    utils.store('http://megatokyo.com/strips/{0}'.format(strip_name), store_path, overwrite=False)

def dump_whole(folder="."):
    for strip_num in xrange(1, last_comic(download=False, return_number=True)+1):
        dump_single(strip_num, folder=folder)

@main.command()
@click.option("--number", help="only valid if action = download")
@click.option("--folder", help="specify a folder to store the dump")
@click.argument("action")
def megatokyo(action, number, folder):
    print(action, number, folder)
    if folder:
        utils.create_folder(folder)
    else:
        folder = "."

    if action == 'dump':
        dump_whole(folder)
    elif action == 'list':
        print("{0} episodes of MegaTokyo have been released".format(last_comic(False, True)))
    elif action == 'download' and number:
        dump_single(int(number), folder=folder)
    else:
        print("unrecognized action (dump, download --number)")
