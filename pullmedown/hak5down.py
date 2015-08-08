#!/usr/bin/env python
import argparse
import re
from .utils import store_ninja, get_page
import click
from . import main
import sys


def store(url):
    html = get_page(url)
    r = re.search('<a class="mov" href="(.+?\/([^\/]+?.mp4))">Download HD<\/a>', html)
    if r:
        print("[~] Downloading " + r.group(1) + " -> " + r.group(2))
        store_ninja(r.group(1), r.group(2))

#parser = argparse.ArgumentParser(description='hak5down, a Hak5 downloader for the masses')
#parser.add_argument('-s', '--season', help='Season', required=True)
#parser.add_argument('-e', '--episode', help='Episode', required=True)
#args = vars(parser.parse_args())

@main.command()
@click.argument("action", type=click.Choice(["season", "ep"]))
@click.argument("season_episode")
def hak5(action, season_episode):
    #print("hak5!", action, season_episode)
    if action == "ep": #args['episode'] == 'ep':
        try:
            season, episode = season_episode.split(".")
        except ValueError as e:
            print("if you ask for a single episode, you have to write <season>.<episode>, with a dot [.]. Please, adjust your input")
            sys.exit(1)
        url = 'http://hak5.org/episodes/hak5-' +  season + episode #args['season'] + args['episode']
        store(url)
    else:
        seasonurl = 'http://hak5.org/category/episodes/season_' + season_episode #args['season']
        #print(seasonurl)
        seasonpage = get_page(seasonurl)
        #for url in re.findall('<a href="(https?:\/\/hak5.org\/episodes\/hak5-' + args['season'] + '\d{2})"', seasonpage):
        for url in re.findall('<a href="(https?:\/\/hak5.org\/episodes\/hak5-' + season_episode + '\d{2})"', seasonpage):
            store(url)
