#!/usr/bin/env python
import urllib.request
import urllib.error
import argparse
import re

def store(url):
    html = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': useragent})).read().decode('utf-8')
    r = re.search('<a class="mov" href="(.+?\/([^\/]+?.mp4))">Download HD<\/a>', html)
    if r:
        print("[~] Downloading " + r.group(1) + " -> " + r.group(2))
        urllib.request.urlretrieve(r.group(1), r.group(2))

parser = argparse.ArgumentParser(description='hak5down, a Hak5 downloader for the masses')
parser.add_argument('-s', '--season', help='Season', required=True)
parser.add_argument('-e', '--episode', help='Episode', required=True)
args = vars(parser.parse_args())

try:
    useragent = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'
    if not args['episode'] == 'dump':
        url = 'http://hak5.org/episodes/hak5-' + args['season'] + args['episode']
        store(url)
    else:
        seasonurl = 'http://hak5.org/category/episodes/season_' + args['season']
        seasonpage = urllib.request.urlopen(urllib.request.Request(seasonurl, headers={'User-Agent': useragent})).read().decode('utf-8')
        for url in re.findall('<a href="(https?:\/\/hak5.org\/episodes\/hak5-' + args['season'] + '\d{2})"', seasonpage):
            store(url)

except urllib.error.HTTPError as err:
    if err.code == 404:
        print('Episode not found (?)')
    else:
        raise
except:
    raise
