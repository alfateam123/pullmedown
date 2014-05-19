import requests
import re
import imgur_downloader as imgur
from os import remove
from shutil import copy2
import sys
from zipfile import ZipFile
from math import log

def format(num, zeroes):
	return "0"*(zeroes-len(str(num)))+str(num)

def getformat(fname):
	return re.findall(".[\w\d]+$", fname)[0]

def docbz(url, name):
	with ZipFile(name+".cbz", "w") as ebook:
		nameslist = imgur.imguralbum(url, True)
		counter=1
		zeroes = int(log(len(nameslist))/log(10))+1 #how many leading zeroes?
		for link in nameslist:
			newname = str(format(counter, zeroes))+getformat(link)
			copy2(link, newname)
			ebook.write(newname)
			remove(newname); remove(link)
			counter += 1

docbz(sys.argv[1], sys.argv[2])


