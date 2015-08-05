#_._ coding:utf-8 _._
import re
from .utils import get_page, store

class MusicForProgrammingDownloader(object):

    def get_episodes(self):
        page = get_page("http://musicforprogramming.net/")
        #removing [u'c=aesthetic', u'c=credits', u'c=donate', u'c=manifesto', u'c=p']
        #as, obviously, they're _not_ episodes.
        return list(url for url in re.findall(r"\/?c=\w+", page) if url not in [u'c=aesthetic', u'c=credits', u'c=donate', u'c=manifesto', u'c=p'])

    def download_episode(self, number):
        try:
            download_episode(get_episodes()[(number.real)-1])
        except AttributeError: #no .real => is _not_ an integer
            page = get_page("http://musicforprogramming.net/?{0}".format("c="+number if not number.startswith("c") else number))
            url, songname = re.findall(r"(http:\/\/datashat\.net\/(music_for_programming_.+\.mp3))\"", page)[0]
            print(url, songname)
            store(url, songname, overwrite=False)

    def download_all(self):
        for i in get_episodes():
            download_episode(i)

    def list_albums(self):
        #print("{0} albums has been released on musicforprogramming".format(len(self.get_episodes())))
        for ep in self.get_episodes():
            print(ep)
