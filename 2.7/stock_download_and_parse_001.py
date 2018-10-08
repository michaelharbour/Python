import sys
import math
import urllib2, zipfile, os


urlToRead = "https://www.nseindia.com/content/historical/EQUITIES/2016/OCT/cm18OCT2016bhav.csv.zip"
localZipFilePath = "/Users/mharbour/python_tests/cm18OCT2016bhav.csv.zip"
# crawledWeb = {}

'''Here is some boilerplate code that we can use to circumvent websites that don't like
bots scraping data off their site.  Usually they attempt to block scripts unless they have
something called the user-agent property set in the HTTP headers'''


#Make the web request - the user agent code above comes into play here.
header = { "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
  "browser": {
    "name": "Chrome",
    "version": "53.0.2785.143",
    "major": "53"
  },
  "engine": {
    "version": "537.36",
    "name": "WebKit"
  },
  "os": {
    "name": "Mac OS",
    "version": "10.11.6"
  },
  "device": {},
  "cpu": {}
}

request = urllib2.Request("http://www.ip-adress.com/ip_tracer/74.82.190.99")
request.add_header("User-Agent", header)

#Check the file using try / except loops.

try:
    page = urllib2.urlopen(request)
    #Save the contents of the zip file to a file called 'content'
    content = page.read()
    #print content
    #Now save the contents locally and open the file.
    output = open(localZipFilePath,"wb")
    #The 'w' indicates that we intend to 'write' to the file.  The 'b' means it's a binary file
    output.write(bytearray(content))
    #Writing the contents to the file.  bytearray() knows how to convert this file into a bytearray
    #that can be written to a file.
    page.close
    #We close the file to make sure that it doesn't become corrupt
except urllib2.HTTPError, e:
    print e.fp.read()
    print "Looks like the file didn't download properly for url = %s\n\n" % urlToRead
    
'''This portion of the scipt will use the zipfile and os libraries to extract the 
zip file.  Unfortun'''

localExtractFilePath = "/Users/mharbour/python_tests"
localExtractFile = "/Users/mharbour/python_tests/testArchive.zip"


if os.path.exists(localExtractFilePath) :
    #print "Great! %s exists...  proceeding.\n\n" % localExtractFilePath
    
    #listOfFiles = []
    
    zip_ref = zipfile.ZipFile(localExtractFile, 'r')
    zip_ref.extractall(localExtractFilePath)
    zip_ref.close()

'''Parse the csv file and create a table of the stock data'''

import csv

oneFileName = "/Users/mharbour/python_tests/goog.csv"


listOfLists = []
#This will take in all the columns from the CSV file as a list

with open(oneFileName, 'r') as csvfile:
#with is a construct that allows us to work with a file without having to explicitly open and close it.

    lineReader = csv.reader(csvfile,delimiter=",",quotechar="\"")
    
    # this is how to skip the header row
    # you execute it before you start iterating
    # over lineReader
    # http://stackoverflow.com/questions/14257373/
    
    next(lineReader,None)
    lineNum = 0
    
    for row in lineReader:
        lineNum = lineNum + 1

    #Everything in life is a list.  The CSV file is a list of lines, and each line is a list of words.
    #We know from the header that:
    #column 1 (index = 0) is the date
    #2 = open, 3 =high, 4 = low, 5 = close, 6 = volume 
    
        name = "NYSE"
        date = row[0]
        open = row[1]
        close = row[4]
        vol = row[5]
        pctChange = float(close)/float(open) - 1
        oneResultRow = [name,date,"{:,.1f}".format(float(vol)/1e6) + "M","{:,.1f}".format(pctChange*100)+"% "]
        listOfLists.append(oneResultRow)
        
        #print name, date, "Percent Change: " + "{:,.1f}".format(pctChange*100)+"% " + "Total Volume: " + "{:,.1f}".format(float(vol)/1e6) + "M"

'''LAMBDA FUNCTIONS are the 'preferred way of doing things Pythonically - they are 'idiomatic' of python.
Basically they are a way of saying, "Dear list, here is a function.  Please apply it to each element of yourself" '''

listOfListsSortedByChng = sorted(listOfLists, key=lambda x:x[3], reverse=True)
#Here we sort the list of lists by column 4 (index = 3).  Reverse=True reverses the sort order

# print listOfListsSortedByVol

import xlsxwriter

excelFileName = "/Users/mharbour/python_tests/testStockSpreadsheet.xlsx"
# create a variable that contains the XLS file that we are going to create

print "\nWe have historical data for the NYSE for the last %03d days, organized by percentage change.\n" % len(listOfLists)
listNum = raw_input("How many of these days would you like to see listed?\n\n")


workbook   = xlsxwriter.Workbook(excelFileName)
worksheet1 = workbook.add_worksheet()


data_b = ("Market", "Pct. Change", "Volume", "Pct. Change")

worksheet1.write('A1' , "NYSE top %d days in the last for the last %d days" % (int(listNum),len(listOfLists))) 
worksheet1.write_row('A2', data_b) 

# The way to write stuff into excel is by specifying:
# a. the cell address (eg A1) in the standard excel format
# b. the list of values to be written, 1 per cell starting from that address.

# Write out the 10 days with the highest percentage change over that day

for num in range(int(listNum)):
    oneRowToWrite = listOfListsSortedByChng[num]
    worksheet1.write_row('A' + str(num + 3), oneRowToWrite)

workbook.close()

print  "\nThank you! Please read the following Excel file:\n\n%s\n\n...to see the top %d movers in the New York Stock Exchange!\n" % (excelFileName, int(listNum))
