#!/usr/bin/env python
import re
import utils
import argparse

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

def dump_single(number, image_format=None):
    if not image_format:
        text = utils.get_page('http://megatokyo.com/strip/{0}'.format(number)) #retrieving the image format
        #print (strip_image(text))
        strip_name = strip_image(text)[0]
    else:
        strip_name = str(number)+image_format
    utils.store('http://megatokyo.com/strips/{0}'.format(strip_name), strip_name, overwrite=False)

def dump_whole():
    for strip_num in xrange(1, last_comic(download=False, return_number=True)+1):
        dump_single(strip_num)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='MegaTokyo downloader')
    parser.add_argument('action', metavar='action', nargs='?', help='Action (dump, download)')
    parser.add_argument('number', metavar='number', nargs='?', help='Issue to be downloaded with the "download" action')
    args = vars(parser.parse_args())

    if args['action'] == 'dump':
        dump_whole()
    elif args['action'] == 'list':
        print("{0} episodes of MegaTokyo have been released".format(last_comic(False, True)))
    elif args['action'] == 'download' and args['number']:
        dump_single(int(args['number']))
    else:
        print('Sounds like you did something wrong... try -h')
