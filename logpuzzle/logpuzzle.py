#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Example: https://code.google.com/edu/languages/google-python-class/images/puzzle/a-baaa.jpg

from asyncore import read
import os
import re
import sys,shutil
import urllib.request as Request


"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""

class LogPuzzle:
  def __init__(self,filename) -> None:
      self.filename = filename
      self.list_links = []
  def read_urls(self):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    

    with open(self.filename,"rt",newline=None) as archiveObj:
      line = archiveObj.readline() 
      while line:
        if 'puzzle' in line:
          pattern = r'GET (\/.*jpg)'
          extract = re.search(pattern,line).group(1)
          if extract not in self.list_links:
            self.list_links.append('https://code.google.com'+extract)
        line = archiveObj.readline()

      self.list_links.sort()
    

  def download_images(self):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    dir = os.path.dirname(__file__)
    os.mkdir(dir+'/page')
    os.mkdir(dir+'/page/images')
    filename = lambda x: os.path.join(dir+'/page/images/',x)
    for i in range (len(self.list_links)):
      Request.urlretrieve(self.list_links[i],filename(f'img{i}.jpg'))


    html_encoding = '<html><head></head><body>%s</body></html>'
    img_enconding_list = [] 
    
    with open('F:\GitHub\google-python-exercises\logpuzzle\page\index.html','w') as htmlObj:
      
      paths = os.listdir(dir+"/page/images")
      ordered  = sorted(paths,key=lambda x:int((re.search('\d+',x).group(0))))
      for path in ordered:
        img_enconding_list.append('<img src="images/%s">' % path)
      htmlObj.write(html_encoding % "".join(img_enconding_list))

    os.startfile('F:\GitHub\google-python-exercises\logpuzzle\page\index.html',)
    shutil.rmtree('F:\GitHub\google-python-exercises\logpuzzle\page')               
    

def main():
  args = sys.argv[1:]

  if not args:
    print ('usage: [--todir dir] logfile')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print ('\n'.join(img_urls))

if __name__ == '__main__':
  #main()
  logpuzzle = LogPuzzle(r'F:\GitHub\google-python-exercises\logpuzzle\animal_code.google.com')
  logpuzzle.read_urls()
  logpuzzle.download_images()
