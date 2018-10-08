import sys
import math
import urllib2

urlToRead = "http://www.google.com"
crawledWeb = {}

while urlToRead != '' :
    try :
        urlToRead = raw_input("Type in the URL you want to download:\n\nJust hit 'return' with nothing entered when you want to stop.\n\n")
        if urlToRead == '':
            print "Ok, exiting loop.\n\n"
            break
        shortName = raw_input("Type in the shortname for this URL %s:\n\n" % urlToRead)
        webFile = urllib2.urlopen(urlToRead).read()
        crawledWeb[shortName] = webFile
    except ValueError as e:
        print "Exception %s trying to parse URL %s.\n(Please try again and make sure it's a full URL.)" % (e, urlToRead)
        traceback.print_exc()
    except urllib2.URLError as e:
        print "Exception %s trying to read from %s. Enter another URL." % (e, urlToRead)
        traceback.print_exc()
        continue
    else:
        print "Okay then, let's continue.\n\n"
        continue

print crawledWeb.values()
