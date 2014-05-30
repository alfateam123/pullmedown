some downloaders I wrote.

they are provided AS IS, and bugs could be around. just keep an eye on them.

Manga
* megatokyo
* batoto (start from the first, it will downloads all the available chapters)
* batoto (one chapter, you have to tell the image link and how many pages. modifiable for fakku)
* mangaeden (just one chapter at the time)

Image-sharing sites
* imgur (downloads albums. be sure you're using /a/ and not /gallery/ )
* imgur (creating a CBZ from the album you download)

Music
* musicforprogramming.net

### U g0+ pr0x1e5? ###
Yup, br0! just configure the `.proxies` file.

this is just a JSON file that contains (protocol, proxy_url) pairs.
in that file, you can configure an "use_useragent" flag: some sites (e.g. mangaeden) perform an user-agent check. my proxy asks for visit confirmation if a browser visits an internet page (and breaks everything if you pretend to be a browser). toggle it (true/false) in case you have troubles using a downloader. 

### I can't download sh*t / It's f***in' broken! ###
Uhm. Before filling an issue, try to play with `.proxies` file, especially the `use_useragent`: try to set it to `false`, maybe you got a proxy blocking you... 

### Dependencies ###
This collection is meant to run on both py2 and py3k.
The only dependency is the Requests library from Kenneth Reitz (you can find it on github, or in the Cheese Shop)