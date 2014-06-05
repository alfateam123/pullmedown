#!/usr/bin/env python
import utils
import re
import sys

def single_image(url, image_index):
    print("visiting url: ", url, image_index)
    p = utils.get_page_ninja(url+"/"+str(image_index))
    diocane= re.findall("<.* id=\"mainImg\" .*>", p)[0]
    #print(diocane)
    #input()
    #mainImg=id
    image, ext = re.findall(r"(cdn\.mangaeden\.com/.+(\.\w{3}))\" .+\>", diocane)[0]
    #print(image)
    #input()
    utils.store_ninja("http://"+image, manganame(url)+"_"+number(url)+"_"+str(image_index)+ext)

def manganame(chapter_url):
    #print("manganame", chapter_url)
    return re.findall(r"\w\w\-manga/([\w\d\-]+)", chapter_url)[0]

def number(chapter_url):
    return re.findall(r"(\d+)/?$", chapter_url)[0]

def pages(chapter_url):
    p = utils.get_page_ninja(chapter_url)
    name, num = manganame(chapter_url), number(chapter_url)
    print( re.findall(name+"/"+num+"/(\d+)", p) )
    return max(int(n) for n in re.findall(name+"/"+num+"/(\d+)", p))

def dump_chapter(chapter_url):
    if not re.findall("\d$", chapter_url):
        print( "add /1")
        dump_chapter(chapter_url+"/1")
    print( "we'll download", pages(chapter_url))
    for i in range(1, pages(chapter_url)+1):
        single_image(chapter_url, i)

dump_chapter(sys.argv[1]) 	
