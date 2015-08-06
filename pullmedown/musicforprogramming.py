#_._ coding:utf-8 _._
import re
from .utils import get_page, store
import feedparser
from collections import namedtuple

MFPAlbum = namedtuple("MFPAlbum", "title link")

class MusicForProgrammingDownloader(object):

    def get_episodes(self):
        feed = feedparser.parse("http://musicforprogramming.net/rss.php")
        return [MFPAlbum(ep.title, ep.id) for ep in feed.entries]

    def download_episode(self, number):
        try:
            self.download_episode_withurl(self.get_episodes()[::-1][(number.real)-1])
        except AttributeError: #no .real => is _not_ an integer
            print("please insert a number. you have inserted {0}, which is of type {1}".format(number, type(number)))

    def download_episode_withurl(self, episode):
        print("downloading episode: {0}".format(episode.title))
        store(episode.link, episode.link.replace("http://datashat.net/", ""))

    def download_all(self):
        for ep in self.get_episodes():
            self.download_episode_withurl(ep)

    def list_albums(self):
        episode_list = self.get_episodes()
        print("{0} albums has been released on musicforprogramming".format(len(episode_list)))
        for ep in episode_list:
            print(ep.title)
