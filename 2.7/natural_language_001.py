import nltk
import matplotlib

# Download some text to play with

from nltk.book import *

'''Here's what get's imported:

*** Introductory Examples for the NLTK Book ***
Loading text1, ..., text9 and sent1, ..., sent9
Type the name of the text or sentence to view it.
Type: 'texts()' or 'sents()' to list the materials.
text1: Moby Dick by Herman Melville 1851
text2: Sense and Sensibility by Jane Austen 1811
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday by G . K . Chesterton 1908

'''

# These are OBJECTS type = 'text'

# 'Concordance will print all of the occurrences of a word along with some context.
# Let's take a look at two texts and check their word usage differences.

print("\n\nThis script will use the super-cool nltk module for Python (the 'Natural Language Toolkit'\n \
to walk through and compare the language from two of the texts listed above.\n")
     
while True:  
    try:
        textSel1 = int(raw_input("Please select the number for the first text you'd like to compare.\n"))
        textSel2 = int(raw_input("Thanks!  Now select the number of the second text to compare.\n"))
        print("Well done!")
        break

    except ValueError as e:
            print "Exception %s\nPlease enter just a number (like '1' or '3')\n" % e
            continue
    #         traceback.print_exc()
textMap = {1:text1, 2:text2, 3:text3, 4:text4, 5:text5, 6:text6, 7:text7, 8:text8, 9:text9}
#print textMap
searchWord = raw_input("\nEnter the word that you would like to compare in the texts.\n")

''' What I couldn't figure out here was how to take the object (which I believe is of the text
class or a text object and use the normal string tools to strip out unwanted characters from the
the readout string - the >Text: bit of the title.

I tried passing the object into a string and then stripping that, but this is impractical because
the list address of the title and author will change dynamically from book to book. 

And I am still not sure why, when passing the object into a variable I get the whole book (the object)
but when calling on the same object in the print fuction using the %s string operator, I only get the 
title and author (along with some of the unwanted formatting stuff hat will not work with the .replace()
operator for ecample because it is an objecty and not a sring.

...sigh...  getting better but still learing.

'''
# bookSelRaw = textMap[textSel1]
# splitBook = [i.split("'") for i in bookSelRaw]
# mySplit = str(splitBook[1:6]).replace("[","").replace("u'","").replace("'],","").replace("]]","").replace("'","")
# print mySplit

print("\n\nHere are examples of how %s uses the word %s\n\n" % (textMap[textSel1],searchWord))
choice1 = "text" + str(textSel1)
#print choice1
textMap[textSel1].concordance(searchWord)

print("\n\nHere are examples of how %s uses the same word,%s\n\n" % (textMap[textSel1],searchWord))
choice2 = "text" + str(textSel2)
#print choice2
textMap[textSel2].concordance(searchWord)

print("\n\nAs you can see, each text uses %s in very different contexts.\nHere are some \
synonyms for %s:\n" % (searchWord, choice1))
       
textMap[textSel1].similar(searchWord)

print("\n\nAnd here are some synonyms for how %s uses it:\n" % choice2)

textMap[textSel2].similar(searchWord)
print("\n")

'''  Use the matplotlib module and the dispersion_plot() to demonstrate how the tool works to show
how a word is disbursed throughout a text'''

text4.dispersion_plot(["citizens","democracy","freedom","duty","America"])

# Testing tokenize()

from nltk.tokenize import word_tokenize, sent_tokenize

text = "Mary had a little lamb.  Her fleese was white as snow."
sents = sent_tokenize(text)
words = [word_tokenize(sent) for sent in sents]
print("Tokenize by sentences:\n%s\nTokenize by words:\n%s\n\n" % (sents,words))


# Play with stopwords

from nltk.corpus import stopwords
from string import punctuation

customStopWords=set(stopwords.words('english')+list(punctuation))
wordsWOStopwords=[word for word in word_tokenize(text) if word not in customStopWords]
print(wordsWOStopwords)
print("\n")

# Play with stemming - 'close' appears in different morphological froms here, stemming will 
# reduce all forms fo the word to its root.  nltk has lots of tools for this.  NLTK also calls
# this lemmatization.

text_2="Mary closed on closing night when she was in the mood to close"
from nltk.stem.lancaster import LancasterStemmer
st=LancasterStemmer()
stemmedWords=[st.stem(word) for word in word_tokenize(text_2)]
print(stemmedWords)
print("\n")

# Use NLTKs ability to tag words by their grammatical notation

myList = [nltk.pos_tag(word_tokenize(text_2))]
for num in myList:
    print("%s\n\n" % num)