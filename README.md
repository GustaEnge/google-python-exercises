# google-python-exercises
## Exercises provided by Google for Education
### link: https://developers.google.com/edu/python/introduction

## [Basic Exercises](https://developers.google.com/edu/python/exercises/basic)

>string1: complete the string functions in string1.py, based on the material in the Python Strings section (additional exercises available in string2.py)

>list1: complete the list functions in list1.py, based on the material in the Python Lists and Python Sorting sections (additional exercises available in list2.py)

>wordcount: this larger, summary exercise in wordcount.py combines all the basic Python material in the above sections plus Python Dicts and Files (a second exercise is available in mimic.py)

## [Baby Name Exercise](https://developers.google.com/edu/python/exercises/baby-names)

>Part A
```
Given a file name for baby.html, returns a list starting with the year string followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
```

>Part B
```
Implement the keyword "summary" in file path to implement a feature which run more than one file at time, looking over the names in all years (tables)
```
## [Copy Special Exercise Modified](https://developers.google.com/edu/python/exercises/copy-special)

>Part A (manipulating file paths)
```
Gather a list of the absolute paths of the special files in all the directories. In the simplest case, just print that list (here the "." after the command is a single argument indicating the current directory). Print one absolute path per line.
```

>Part B (file copying)
```
If the "--todir dir" option is present at the start of the command line, do not print anything and instead copy the files to the given directory, creating it if necessary. Use the python module "shutil" for file copying.
```

>Part C (calling an external program)
```
If the "--tozip zipfile" option is present at the start of the command line, run this command: "zip -j zipfile <list all the files>". This will create a zipfile containing the files. Just for fun/reassurance, also print the command line you are going to do first (as shown in lecture). (Windows note: windows does not come with a program to produce standard .zip archives by default, but you can get download the free and open zip program from www.info-zip.org.)
```
> Tips:
```
You can reach the usage by performing the method --help
```

## [Log Puzzle Exercise](https://developers.google.com/edu/python/exercises/log-puzzle)

>Part A - Log File To Urls
```
Complete the read_urls(filename) function that extracts the puzzle urls from inside a logfile. Find all the "puzzle" path urls in the logfile. Combine the path from each url with the server name from the filename to form a full url, e.g. "http://www.example.com/path/puzzle/from/inside/file". Screen out urls that appear more than once.
```

>Part B - Download Images Puzzle
```
Complete the download_images() function which takes a sorted list of urls and a directory. Download the image from each url into the given directory, creating the directory first if necessary, the function should also create an index.html file in the directory with an *img* tag to show each local image file
```

>Part C - Image Slice Descrambling
```
The second puzzle involves an image of a very famous place, but depends on some custom sorting. For the first puzzle, the urls can be sorted alphabetically to order the images correctly. In the sort, the whole url is used. However, we'll say that if the url ends in the pattern "-wordchars-wordchars.jpg", e.g. "http://example.com/foo/puzzle/bar-abab-baaa.jpg", then the url should be represented by the second word in the sort (e.g. "baaa"). So sorting a list of urls each ending with the word-word.jpg pattern should order the urls by the second word.
```