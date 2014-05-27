#!/usr/bin/env python
import os
import re
from zipfile import ZipFile
import sys
import shutil
from math import log

def format(num, zeroes):
	return "0"*(zeroes-len(str(num)))+str(num)

def getformat(fname):
	return re.findall(".[\w\d]+$", fname)[0]

if __name__ == "__main__":
	folderpath = sys.argv[1]
	counter = 1

	with ZipFile(folderpath+".cbz", "w") as ebook:
		for path, dirs, files in os.walk(folderpath):
			files = [re.sub("Page_0(\d)", r"Page_\1", file_) for file_ in 
						sorted([re.sub("Page_(\d)_", r"Page_0\1_", file_) for file_ in files])
					]
			zeroes = int(log(len(files))/log(10))+1 #how many leading zeroes?
			for file_ in files:
				#print (file_)
				shutil.copy(os.path.join(path, file_), format(counter, zeroes)+getformat(file_))
				ebook.write(format(counter, zeroes)+getformat(file_))
				os.remove(format(counter, zeroes)+getformat(file_))
				counter += 1
			counter = 1
