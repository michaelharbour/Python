import nltk
import matplotlib

from bs4 import BeautifulSoup as BS

''' This lesson will be about scraping web pages to get the data we need to use our natural language
processing tools on'''

html=['<html><heading style="font-size:20px"><i>This is the title<br><br></i></heading>',
     '<body><b>This is the body</b><p id="para1">This is para1<a href="www.google.com">Google</a></p>',
     '<p id="para2">This is para 2</p></body></html>']
html=''.join(html)

# print(html)

soup = BS(html, "html.parser")
# print(soup.prettify())

print(soup.html.name)

print(soup.body.name)

print(soup.body.text)

paras = ' '.join([p.text for p in soup.findAll('p')])
print(paras)

# Links are generally in the form of <a href='link'>'link-text'</a>

links = soup.find('a')

print(links)

print(links['href']+" is the url and "+links.text+" is the text")

# Let's say that you want the texty of the first paragraph after the firsts occurance of 'Google'.

myLine = soup.find(text="Google").findNext('p').text
 
print(myLine)