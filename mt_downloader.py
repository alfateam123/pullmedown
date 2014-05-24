import requests
import re
import utils

"""
Downloader for MegaTokyo webcomic.
"""

# py3k compatibility
xrange = range if not ( 'xrange' in dir(__builtins__) ) else xrange

strip_image = lambda text: re.findall('src\="strips\/(\d+\.\w+)"', text)

def last_comic(download=True, return_number=False):
    r = requests.get('http://megatokyo.com')
    print (strip_image(r.text))
    strip_number = int(strip_image(r.text)[0][:-4]) #removing .png || .gif
    if download:
        dump_single(strip_number, image_format=strip_image(r.text)[0][-4:]) 
    if return_number:
        return strip_number

def dump_single(number, image_format=None):
    if not image_format:
        r = requests.get('http://megatokyo.com/strip/{0}'.format(number)) #retrieving the image format
        print (strip_image(r.text))
        strip_name = strip_image(r.text)[0]
    else:
        strip_name = str(number)+image_format
    utils.store('http://megatokyo.com/strips/{0}'.format(strip_name), strip_name, overwrite=False)

def dump_whole():
    for strip_num in xrange(1, last_comic(download=False, return_number=True)+1):
        dump_single(strip_num)

if __name__=="__main__":
    print ("last comic number is: ", last_comic(download=False, return_number=True))
    dump_whole();

