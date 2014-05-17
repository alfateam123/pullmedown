import requests
import re

strip_image = lambda text: re.findall('src\="strips\/(\d+\.\w+)"', text)

if __name__=="__main__":
    for i in xrange(1, 1397+1):
      print "i: ", i
      r = requests.get('http://megatokyo.com/strip/{0}'.format(i))
      print strip_image(r.text)
      strip_name = strip_image(r.text)[0]
      image_content = requests.get('http://megatokyo.com/strips/{0}'.format(strip_name))
      with open(strip_name, 'wb') as fd:
          for chunk in image_content.iter_content(1024*10):
              fd.write(chunk)


      print "finished ", strip_name
