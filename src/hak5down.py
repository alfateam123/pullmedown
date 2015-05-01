#!/usr/bin/env python
import argparse
import re
import utils

def store(url):
    html = utils.get_page_ninja(url)
    r = re.search('<a class="mov" href="(.+?\/([^\/]+?.mp4))">Download HD<\/a>', html)
    if r:
        print("[~] Downloading " + r.group(1) + " -> " + r.group(2))
        utils.store_ninja(r.group(1), r.group(2))

parser = argparse.ArgumentParser(description='hak5down, a Hak5 downloader for the masses')
parser.add_argument('-s', '--season', help='Season', required=True)
parser.add_argument('-e', '--episode', help='Episode', required=True)
args = vars(parser.parse_args())

try:
    if not args['episode'] == 'dump':
        url = 'http://hak5.org/episodes/hak5-' + args['season'] + args['episode']
        store(url)
    else:
        seasonurl = 'http://hak5.org/category/episodes/season_' + args['season']
        seasonpage = utils.get_page_ninja(seasonurl)
        for url in re.findall('<a href="(https?:\/\/hak5.org\/episodes\/hak5-' + args['season'] + '\d{2})"', seasonpage):
            store(url)

except:
    raise
