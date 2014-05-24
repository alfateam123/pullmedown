from os.path import exists
import requests

def store(url, pathname, overwrite=True):
	if overwrite or not exists(pathname):
		print ("[utils.store]", "saving the file")
		image_content = requests.get(url)
		with open(pathname, 'wb') as fd:
			for chunk in image_content.iter_content(1024*(10**3)):
				fd.write(chunk)
	print ('[utils.store]: url=', url)
