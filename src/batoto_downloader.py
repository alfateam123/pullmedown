#!/usr/bin/env python
import requests, re, utils
import sys

next_and_img = lambda req_text: re.findall("(.+)\n.+\<img id=\"comic_page\" (.+)\>", req_text, re.MULTILINE)[0]

next_link = lambda next_tag: re.findall("href=\"(.+)\"", next_tag)[0]
img_link = lambda img_tag: re.findall("src=\"(.+\.\w+)\" ", img_tag)[0]
alt_tag = lambda img_tag: re.findall("alt=\"([()\w\s-]+)", img_tag)[0].replace(" ", "_")
img_format = lambda imglink: re.findall("\.\w+$", imglink)[0]

if __name__=="__main__":
    found_next = True
    link = sys.argv[1] #"http://www.batoto.net/read/_/181322/kagerou-daze_chspecial_by_gei-manga"
    while found_next:
        print ("muh link: ", link)
        text = utils.get_page(link)
        #print ("debug: ", next_and_img(r.text))
        nexttag, imgtag = next_and_img(text)
        link = next_link(nexttag)
        print ("next link is: ", link)
        title, imagelink = alt_tag(imgtag), img_link(imgtag)
        print ("title is", title, "imagelink is: ", imagelink)
        print ("debug: ",  re.findall("\.\w+$", imagelink))
        utils.store(imagelink, title+img_format(imagelink), overwrite=False)
