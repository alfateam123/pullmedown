import utils
import feedparser

def episode_list():
    feed = feedparser.parse("http://digitalia.fm/feed/")
    return feed.entries

def dump_last():
	ep = episode_list()[0]
	ep_link = ep.links[-1]["href"]
	utils.store(ep_link, ep.title.replace(" ", "_")+".mp3")

if __name__ == '__main__':
    print "last episodes: "
    for ep in episode_list():
        print ep.title
    print "dumping last"
    dump_last()	
