Some downloaders I wrote, united under a single executable.

Manga
* [SOON] megatokyo
* [SOON] batoto (start from the first, it will downloads all the available chapters)
* [SOON] batoto (one chapter, you have to tell the image link and how many pages. modifiable for fakku)
* [SOON] mangaeden (just one chapter at the time)
* fakku (n  free content anymore, didn't subscribe to check legit downloads)

sadpanda won't be supported, unless a saduser files a PR to add it.

Image-sharing sites
* imgur (downloads albums. be sure you're using /a/ and not /gallery/ )

Music
* musicforprogramming.net

Video
* hak5.org

Audio podcasts
* [SOON] digitalia.fm

Utilities
* [SOON] epub to cbz
* [SOON] folder to cbz


### U g0+ pr0x1e5? ###
Yup, br0! just create a `.proxies` file.

```
#example of .proxies file
{
  "http": "http://user:password!@proxy.address:8081",
  "use_useragent": true
}
```

In that file, you can configure an "use_useragent" flag: some sites (e.g. mangaeden) perform an user-agent check.
my work proxy asks for visit confirmation ("I accept to visit this stackoverflow page, knowning I'll be spied by my organization") if a browser visits an internet page (and breaks everything if you pretend to be a browser). Toggle it (true/false) in case you have troubles using a downloader. 

### w-will it work on my favourite Python version? ###

`pullmedown` is meant to work on Py2 and Py3 with a single codebase. If it does not work, open an issue at our github repository.
