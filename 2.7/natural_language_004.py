import urllib2
from bs4 import BeautifulSoup as BS

def getOnlyTextWP(url):
    # Uses urllib to download html page and BS  to scrape out the text we want
    page = urllib2.urlopen(url).read().decode('utf8')
    # open the page
    soup = BS(page, 'html.parser')
    # dump the contents to the page
    text = ' '.join(map(lambda p: p.text, soup.find_all('article')))
    # use the code to get all the text that lies between the <article> stuff </article>
    # HTML tags.  This is specific to the URL here (Washington Post) and will change
    # depending on the website.
    soup2 = BS(text, 'html.parser')
    # Now that we have the article.  Pare this down to the actual text between the 
    # <p> </p> paragraph tags.  Again, this is dependent on the website's conventions.
    text = ' '.join(map(lambda p: p.text, soup2.find_all('p')))
    return soup.title.text, text
    # This will take a URL that corresponds to the following format:
    # <html> <title> Article Headline </title>
    # <body> [stuff] <article> <p> para 1</p> <p> para 2 </p> </article>
    # </body>
    # This function should return a pair ('Article Headline', 'para 1 para 2')
    
someUrl = "https://www.washingtonpost.com/news/worldviews/wp/2016/11/08/in-rare-blast-at-british-media-prince-harry-says-his-american-girlfriend-meghan-markle-faces-wave-of-abuse/?hpid=hp_hp-more-top-stories_wv-harry-850am%3Ahomepage%2Fstory"
textOfUrl = getOnlyTextWP(someUrl)
print(textOfUrl)