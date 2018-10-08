from bs4 import BeautifulSoup as BS
import urllib2
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import matplotlib
import requests
import string
import collections
from math import log

from heapq import nlargest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans





#################################################################################
#
# SETUP YOUR FUNCTIONS
#
#################################################################################

class frequencySummarizer:
    def __init__(self,min_cut=0.1,max_cut=0.9):
    # Class construction - takes in min and max cutoffs for frequency
        self._min_cut = min_cut
        self._max_cut = max_cut
        self._stopwords = set(stopwords.words('english') + list(string.punctuation) + [u"'s",'"'])
        # stopwords are a set - not a list.  It's easy to go from set to list and vice-versa
        # use the set() and list() functions
        # conceptually sets are different from lists because sets don't have an order
        # while lists do
    
    def _compute_frequencies(self, word_sent,freq,customStopWords=None):
#         print word_sent
#         freq = collections.defaultdict(int)
        # defaultdict is a standard dictionary
        if customStopWords is None:
            stopwords = set(self._stopwords)
        else:
            stopwords = set(customStopWords).union(self._stopwords)
        newStopWords = ['new', 'york', 'times', 'washington', 'post','-']
        for newWord in newStopWords:
            stopwords.add(newWord)
        for sentence in word_sent:
            for word in sentence:
                if word not in stopwords:
                    freq[word] += 1
                    print word + "\t" + str(freq) + "\n\n"
                    
#         flattened = [val for sublist in collectAll for val in sublist]
#         flattenedAgain = [val for sublist in flattened for val in sublist]
#         print flattenedAgain

        m = float(max(freq.values()))
        for word in freq.keys():
            freq[word] = freq[word]/m
            if freq[word] >= self._max_cut or freq[word] <= self._min_cut:
                del freq[word]
        return freq
               
    
    def extractFeatures(self,article,n,freq,customStopWords=None):
        # The article is passed in as a tupe (text, title)
        text = article[0]
#         print str(article[0]) + " = text\n"
        # extract the text
        title = article[1]
#         print article[1] + " = title\n"
        # extract the title
        sentences = sent_tokenize(title)
#         print str(sentences) + " = sentences\n"
        # split the text into two sentences
        word_sent = [word_tokenize(s.lower()) for s in sentences]
#         print str(word_sent) + " = word\n\n\n\n" 
        #split the sentences into words
#         freq = collections.defaultdict(int)
        self._freq = self._compute_frequencies(word_sent,freq,customStopWords)
#         if self._freq is not None:
#             print self._freq
#         Calculate the word frequencies using the member function
        if n < 0:
        # How many features to return?
            return nlargest(len(self._freq_keys()),self._freq,key= self._freq.get)
        else:
            # if the calling function has called for a subset, only return 'n' largest
            # features - important words (e.g. the most frequent)
#             print self._freq
            return nlargest(n,self._freq,key=self._freq.get) 



    def extractRawFrequencies(self,article):
        # very similar to extractFeatures() but will just return the words counts
          # The article is passed in as a tupe (text, title)
        text = article[0]
        # extract the text
        title = article[1]
        # extract the title
        sentences = sent_tokenize(text)
        # split the text into two sentences
        word_sent = [word_tokenize(s.lower()) for s in sentences]
        #split the sentences into words
        freq = collections.defaultdict(int)
        for s in word_sent:
            for word in s:
                if word not in self._stopwords:
                    freq[word] += 1
        return freq
    
    
    
    def summarize(self, article,n):
        text = article[0]
        # extract the text
        title = article[1]
        # extract the title
        sentences = sent_tokenize(text)
        # split the text into two sentences
        word_sent = [word_tokenize(s.lower()) for s in sentences]
        #split the sentences into words
        self._freq = self._compute_frequencies(word_sent,customStopWords)
        # Calculate the word frequencies using the member function
        ranking = collections.defaultdict(int)
        for i, sentence in enumerate(word_sent):
            for word in sentence:
                if word in self._freq:
                    ranking[i] += self._freq[word]
        sentences_index = nlargest(n,ranking,key=ranking.get)
        return [sentences[j] for j in sents_idx]


def getWashPostText(url,token):
    req = urllib2.Request(url, headers=hdr)
    try:
        page = urllib2.urlopen(req).read().decode('utf8')
    except:
        return(None,None)
    soup = BS(page,"html.parser")
    if soup is None:
        return(None,None)    
    text = ""
    if soup.find_all(token) is not None:
        text = ''.join(map(lambda p: p.text, soup.find_all(token)))
        soup2 = BS(text, "html.parser")
        if soup2.find_all('p') is not None:
            text = ''.join(map(lambda p: p.text, soup2.find_all('p')))  
    return text, soup.title.text
 
    
    
def getNYTText(url,token):

    response = requests.get(url)
    soup = BS(response.content, "html.parser")
    page = str(soup)
    title = soup.find('title').text
    
#   mydivs = soup.findAll("p", {"class":"story-body-text story-content"})
    mydivs = soup.findAll("p", {"class":"summary"})

    text = ''.join(map(lambda p:p.text, mydivs))
#     print text

    
    return text, title
   

def scrapeSource(url,hdr,magicFrag='2016',scraperFunction=getNYTText, token='None'):

    urlBodies = {}
    request = urllib2.Request(url, headers=hdr)
    response = urllib2.urlopen(request)
    soup = BS(response, "html.parser")
    
#     print soup
    
    numErrors = 0
    for a in soup.findAll('a'):
        try:
            url = a['href']
            
#             print url
            
            if (url not in urlBodies) and (magicFrag in url):
                #and
                #((magicFrag is not Nine and magicFrag in url)
                #or magicFrag is None)):
#                 print url          
                      
                body = scraperFunction(url, token)
                
#                 print body
                
                if body and len(body) > 0:
                    urlBodies[url] = body
        except:
            numErrors += 1
#     print urlBodies       
    return urlBodies
    
# def getDoxyDonkeyText(testUrl,token):
#     response = requests.get(testUrl)
#     soup = BS(response.content, "html.parser")
#     page = str(soup)
#     title = soup.find("title").text
#     mydivs = soup.findAll("div", {"class":token})
#     text = ''.join(map(lambda p:p.text,mydivs))
#     return text,title
#     # This is a test instance we can use before going into our real data
#     # setup as a (title, text) tuple
#     
# testUrl = "http://doxydonkey.blogspot.in"
# testArticle = getDoxyDonkeyText(testUrl,"post-body")
# 
# fs = frequencySummarizer()
# testArticleSummary = fs.extractFeatures(testArticle, 25)


#################################################################################
#
# Some bogus header information to bypass website security
#
#################################################################################


#Make the web request - the user agent code above comes into play here.
hdr = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*q=0.8',
       'Accept-Charset':'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
       'Accept-Encoding':'none',
       'Accept-Language':'en-US,en;q=0.8',
       'Connection':'keep-alive'
      }
    
#################################################################################
#
# DO SOMETHING WITH YOUR FUNCTIONS
#
#################################################################################


urlWashingtonPostNonTech = "https://www.washingtonpost.com/sports/"
urlNewYorkTimesNonTech = "https://www.nytimes.com/pages/sports/index.html"
urlWashingtonPostTech = "https://www.washingtonpost.com/technology/"
urlNewYorkTimesTech = "https://www.nytimes.com/pages/technology/index.html"

washingtonPostTechArticles = scrapeSource(urlWashingtonPostTech,hdr,'2016', getWashPostText, 'article')
washingtonPostNonTechArticles = scrapeSource(urlWashingtonPostNonTech,hdr,'2016', getWashPostText, 'article')

newYorkTimesTechArticles = scrapeSource(urlNewYorkTimesTech,hdr,'2016', getNYTText, None)
newYorkTimesNonTechArticles = scrapeSource(urlNewYorkTimesNonTech,hdr,'2016', getNYTText, None)

# test = "u\'http://www.nytimes.com/2016/11/16/business/tech-distractions-blamed-for-rise-in-traffic-fatalities.html?ref=technology\'"
# myKeys = newYorkTimesTechArticles.keys()
# print newYorkTimesTechArticles[myKeys[0]]
# getNYTText(urlNewYorkTimesTech,'2016')

articleSummaries = {}
freq = collections.defaultdict(int)
# freq = collections.defaultdict(int)



for techUrlDictionary in [newYorkTimesTechArticles, washingtonPostTechArticles]:
#     if len(techUrlDictionary) > 0:
#         x = 0
#         while x < len(techUrlDictionary) :
#             myKeys = techUrlDictionary.keys()
#             print str(techUrlDictionary[myKeys[x]]).replace("(u\'","")\
#             .replace("\')","")\
#             .replace("(\'\', u\'","").replace("\\u2018","`").replace("\\u2019","\'")\
#             + "\n\n"
            
#             x = x + 1

#     num = 1
#     for key, value in  techUrlDictionary.iteritems() :
#         print str(num) + "\n" + str(key).replace("?ref=technology","").replace("?src=me","").replace("?src=mv","")\
#          + "\n" + str(value).replace("(u\'","")\
#         .replace("\')","")\
#         .replace("(\'\', u\'","").replace("\\u2018","`").replace("\\u2019","\'")\
#          + "\n\n"
#     
#         num = num + 1

#     num = 1
#     for articleUrl in newYorkTimesTechArticles:

    
    for articleUrl in techUrlDictionary:
        if (len(techUrlDictionary[articleUrl]) > 0) and (len(techUrlDictionary[articleUrl]) is not None):
#             print str(techUrlDictionary[articleUrl]).replace("(\'\', u\'","").replace("\')","")\
#             .replace("(u\'","").replace("(\'\'","").replace("\\u2014","--").replace("\\u2018","`").replace("\\u2019","\'")\
#             + "\n\n"
#         if ((len(techUrlDictionary[articleUrl][0]) > 0) and (len(techUrlDictionary[articleUrl][ 0]) is not None)):
#         print str(num) + "\t" + articleUrl + "\n" 
#         num = num + 1

# num = 0
# for key, value in  newYorkTimesTechArticles.iteritems() :
#     print str(num) + "\n" + str(key).replace("?ref=technology","").replace("?src=me","").replace("?src=mv","")\
#      + "\n" + str(value).replace("(u\'","")\
#     .replace("\')","")\
#     .replace("(\'\', u\'","").replace("\\u2018","`").replace("\\u2019","\'")\
#      + "\n\n"
#     
#     num = num + 1


            fs = frequencySummarizer()
#             temp = techUrlDictionary[articleUrl]
#             print str(temp[0]) + "\n\n\n\n" + temp[1] + "\n\n\n\n"
#             print techUrlDictionary[articleUrl]
            summary = fs.extractFeatures(techUrlDictionary[articleUrl],10,freq)
#             print summary
            articleSummaries[articleUrl] = {'feature-vector': summary,'label':'Tech'}
            
            
#             
#             
# for nontechUrlDictionary in [newYorkTimesNonTechArticles, washingtonPostNonTechArticles]:
#     for articleUrl in newYorkTimesTechArticles:
#         if (len(nontechUrlDictionary[articleUrl][0]) > 0 and len(nontechUrlDictionary[articleUrl][0]) is not None):
#             fs = frequencySummarizer()
#             summary = fs.extractFeatures(nontechUrlDictionary[articleUrl],5)
#             articleSummaries[articleUrl] = {'feature-vector':summary,'label':'Non-Tech'}
    
    
#################################################################################
#
# PLAY WITH THE OUTPUT
#
#################################################################################

# print articleSummaries

# for i in articleSummaries:
#     print("%s\t%\n" % str(articleSummaries[i]))

# num = 1
# for key, value in  articleSummaries.iteritems() :
#     print str(num) + "\n" + str(key) + "\n" + str(value) + "\n\n"
#     num += 1