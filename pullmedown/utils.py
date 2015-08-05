from os.path import exists
import requests
import json

def proxies():
    try:
        return json.load(open(".proxies"))
    except IOError:
        return {}

def use_useragent():
    try:
        return proxies()["use_useragent"]
    except KeyError:
        return False

def store_ninja(url, pathname, overwrite=True):
    if overwrite or not exists(pathname):
        r=requests.Request(
            'GET', url,
            headers={
                'User-Agent': "" if not use_useragent() else 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
                'Accept-Encoding': 'gzip, deflate',
                'Accept': '*/*'}
        )
        prep=r.prepare()
        s=requests.Session()
        image_content=s.send(prep, stream=True, proxies=proxies())
        with open(pathname, 'wb') as fd:
            for chunk in image_content.iter_content(1024*(10**3)):
                fd.write(chunk)
    print ("[utils.store]: url=", url)

def get_page_ninja(url, is_json=False, method="get", parameters=None):
    r=requests.Request(
        method.upper(),
        url,
        data = parameters or [],
        headers={'User-Agent': "" if not use_useragent() else  'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*'},
    )
    prep=r.prepare()
    s=requests.Session()
    resp=s.send(prep, proxies=proxies())
    return resp.json() if is_json else resp.text

store = store_ninja
get_page = get_page_ninja
