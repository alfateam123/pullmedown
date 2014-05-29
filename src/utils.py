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

def store_ninja(url, pathname, overwrite=True):
    if overwrite or not exists(pathname):
        r=requests.Request('GET', url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*'})
        prep=r.prepare()
        s=requests.Session()
        image_content=s.send(prep, stream=True)
        with open(pathname, 'wb') as fd:
            for chunk in image_content.iter_content(1024*(10**3)):
                fd.write(chunk)
    print ("[utils.store_ninja]: url=", url)

def get_page(url, is_json=False, method="get", parameters=None):
    try:
        r = {"get" : requests.get, "post": requests.post}[method.lower()](url, data=parameters)
    except KeyError:
        raise ValueError("method passed is not GET or POST")
    return r.json() if is_json else r.text

def get_page_ninja(url, is_json=False):
    r=requests.Request('GET', url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*'})
    prep=r.prepare()
    s=requests.Session()
    resp=s.send(prep)
    return resp.json() if is_json else resp.text
