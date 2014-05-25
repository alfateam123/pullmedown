import utils
import re
import sys

def get_episodes():
	page = utils.get_page("http://musicforprogramming.net/")
	#removing [u'c=aesthetic', u'c=credits', u'c=donate', u'c=manifesto', u'c=p']
	#as, obviously, they're _not_ episodes.
	return re.findall(r"\/?c=\w+", page)[:-5]

def download_episode(number):
	try:
		download_episode(get_episodes()[(number.real)-1])
	except AttributeError: #no .real => is _not_ an integer
		page = utils.get_page("http://musicforprogramming.net/?{0}".format("c="+number if not number.startswith("c") else number))
		url, songname = re.findall(r"(http:\/\/datashat\.net\/(music_for_programming_.+\.mp3))\"", page)[0]
		print( url, songname )
		utils.store(url, songname, overwrite=False)

def download_all():
	for i in get_episodes():
		download_episode(i)

if __name__ == '__main__':
	if sys.argv[1] == '--dump':
		download_all()
	elif sys.argv[1] == '--number':
		print( "actually, {0} episodes of Music for Programming have been released".format(len(get_episodes())) )
	elif sys.argv[1] == '--last':
		download_episode(len(get_episodes()))
	else:
		download_episode(int(sys.argv[1]))