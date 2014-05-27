from os.path import exists
import requests

def store(url, pathname, overwrite=True):
    if overwrite or not exists(pathname):
        print ("[utils.store]", "saving the file")
        image_content = requests.get(url, stream=True)
        with open(pathname, 'wb') as fd:
            for chunk in image_content.iter_content(1024*(10**3)):
                fd.write(chunk)
    print ('[utils.store]: url=', url)

def get_page(url, is_json=False, method="get", parameters=None):
    try:
        r = {
	      "get" : requests.get,
              "post": requests.post
	}[method.lower()](url, data=parameters)
    except KeyError:
        raise ValueError("method passed is not GET or POST")
    return r.json() if is_json else r.text
