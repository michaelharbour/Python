import math
import sys

'''The idea of this tutorial is to creat e program similar to what a bank ATM would do.  Initially
it might seems like lists and dictionaries would be a good way to keep track of users account
numbers and balances but, as these are stored in memory, this is a terrible idea for a bank which must
always be able to account for the last transaction regardless of what happened to the program, as 
well as talk to all the other ATMs so that people can't take advantage of this data not being
centrilized.  It is for this reason that we need to look to work with files and/or databases.

While files can work, they can be a headache to deal with when you have a large number of clients
on a single server.  DBMS (Database Management Systems) were designed with this specifically in mind
and have developeded ways of working around the inherent problems in files.  This is what you would
use in the case of something like am ATM

Databases work with 'Tables' which are made up of rows and columns generally.  Most of what a database 
does is creating these tables, checking data in and out of it and allowing for seemless modification
of the extracted data before putting it back in or taking it out.

"Querying" is the process of reading (but not writing) from a table.  This is generally done using
SQL (Structured Query Language).  SQL is a languarge that is understood by all DBMS and basically is 
designed to do the basic 8 functions (making tables, adjusting tables, querying tables, putting
modified data back into tables, etc.) required for working with a DBMS

The SCHEMA of a table refers to it's main three components which are the 'Primary Key' (the id for
that table, references to that table, and the fact that it is not NULL (which is exactly like
NONE in python.

We will use SQLITE which is a software library that implements a 'self-contained, serverless
zero-configuration, transactional SQL database engine.  Python uses the 'sqlite3 module.  This
doesn't need to be installed using !pip or conda - just imprt the module and it is good to go

I had to modify a bit because the zip files downloaded from the provided website are not proper zip files.
The CSV I created in OSX would give the following error:

new-line character seen in unquoted field - do you need to open the file in universal-newline mode?

...the solution (one, at least) was to save as a Windows CSV file

So, while each step of the process works, I couldn't do it with the files that were provided and 
had to sometimes make some modificatons to get it all to work. '''

########################################################################
# Step 1.  Create a table in our database to hold the stock information
########################################################################

import urllib2, cookielib
import zipfile, os
import csv
import time
import sqlite3
from datetime import datetime

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table

c.execute('CREATE TABLE prices (SYMBOL text, SERIES text, OPEN real, HIGH real, LOW real, CLOSE real, LAST real, PREVCLOSE real, TOTTRDQTY real, TOTTRDVAL real, TIMESTAMP date, TOTALTRADES real, ISIN text, PRIMARY KEY (SYMBOL, SERIES, TIMESTAMP))')
conn.commit()


########################################################################
# Step 2.  Download the data
########################################################################

def download(localZipFilePath,urlOffName):
#     urlToRead = "https://www.nseindia.com/content/historical/EQUITIES/2016/OCT/cm18OCT2016bhav.csv.zip"
#     localZipFilePath = "/Users/mharbour/python_tests/cm18OCT2016bhav.csv.zip"
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


def unzip(localZipFilePath,localExtractFilePath):
    '''This portion of the scipt will use the zipfile and os libraries to extract the 
    zip file.'''

    localExtractFilePath = "/Users/mharbour/python_tests"
    localExtractFile = "/Users/mharbour/python_tests/PR010114.zip" 


    if os.path.exists(localExtractFilePath) :
        print "Great! %s exists...  proceeding.\n\n" % localExtractFilePath
    
        #listOfFiles = []
    
        zip_ref = zipfile.ZipFile(localExtractFile, 'r')
        zip_ref.extractall(localExtractFilePath)
        zip_ref.close()
        
def downloadAndUnzipForPeriod(listOfMonths, listOfYears):
    for year in listOfYears:
        for month in listOfMonths:
            for dayOfMonth in xrange(31):
                date = dayOfMonth + 1
                #########################################################################################
                # The following code constructs the URL for the India Stock Exchange which has 
                # URLs that typicaly look like this:
                # https://www.nseindia.com/content/historical/EQUITIES/2016/OCT/cm18OCT2016bhav.csv.zip
                #########################################################################################
                
                dateStr = str(date)
                if date < 10:
                    dateStr = "0" +dateStr #force the date to be 2-pad
                print dateStr, "-", month,"-", year
                # Construct the filename
                fileName = "cm" +str(dateStr) + str(month) + str(year) + "bhav.csv.zip"
                # Construct the URL
                urlOfFileName = "http://www.nseindia.com/content/historical/EQUITIES/" + year + "/" + month + "/" + fileName
                # Construct local path for the downloaded file
                localZipFilePath = "/Users/mharbour/python_tests/" + fileName
#                 localExtractFilePath = "/Users/mharbour/python_tests/"
                # Make the call to the download function
                download(localZipFilePath,urlOfFileName)
                
                '''I turned off the unzip portion, which works, but is creating a lot of
                csv files that don't match the formatting of the 'ideal' csv in the insertRows
                module'''
#                 unzip(localZipFilePath,localExtractFilePath)

                # We want to make sure that we don't do a DOS attack on the indian stock excange
                # so we take a pause of 10 seconds before repeating code.
                time.sleep(3)
    print "Ok, all down downloading and extracting.\n\n"
    
# initalize a variable with a local directory in whihc to extact the zip file above

localExtractFilePath = "/Users/mharbour/python_tests/"


listOfMonths = ['JAN']
listOfYears = ['2014']

'''!!!!  This is the function to download and unzip your data - unfortunately the data it downloads is not
actually a .zip file so I have to download something explicit and change the code to point to it so that
I have something to work on.  I am turning off for the moment to work on the next fuction to edit tables'''

'''This is commented out while working on the latter part of the script so that I don't
have to wait for it to download the files each time before moving on.'''
# downloadAndUnzipForPeriod(listOfMonths,listOfYears)

def insertRows(fileName,conn):
    # conn is a connection to the database
    # given a connection, we need a session in which to do stuff
    c = conn.cursor()
    lineNum = 0
    with open(fileName, 'rb') as csvfile:
        # The file is open.  :et's get a CSV handler.  The handler needs to be told how strings in quotes
        # will appear - we tell it that quotes will be marked with double quotes.
        lineReader = csv.reader(csvfile, delimiter = ',', quotechar = "\"",dialect=csv.excel_tab)
        # Ok!  The CSV handler called 'lineReader' knows how to read a file 1 line at a time
        # Iterate using a for loop and the iterator variable 'row'
        
        for row in lineReader:
            print row
            # What line are we on?  Increase the counter by 1
            lineNum = lineNum + 1
            # if this was the first line - which contains a header - skip and go to the next via
            # the 'continue' statement.
            if lineNum == 1:
                print "Header Row.  Skipping...\n"
                continue
            # Insert a row of data
#             date_object = datetime.strptime(row[10], '%d-%b-%Y)
            date_object = "10-10-2016"
            print row[10]
            ##############################################################################
            # We just wrote to the database, so we must commit our writes
            ##############################################################################
            # We will insert data into the database 1 row at a time.  This data must correspond in the 
            # number and type to the column headers of the table.  The columns in a table are
            # collectively called the schema
            oneTuple = [row[0], row[1], float(row[2]), float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), float(row[8]), float(row[9]), date_object, float(row[11]), row[12]]
            # This statement inserts one row into the table
            c.execute("INSERT INTO prices VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", oneTuple)
        conn.commit()
        print "Done iterating over file contents - the file is now closed\n\n"
        
for file in os.listdir(localExtractFilePath):
    if file.endswith(".csv"):
        insertRows(localExtractFilePath+file,conn)
        print localExtractFilePath+file


##########################################################################
# Test that your data was parsed into the database okay
##########################################################################

t1 = 'NTPC'
series = 'N6'
c = conn.cursor()
cursor = c.execute ('SELECT symbol, max(close), min(close),max(timestamp), min(timestamp), count(timestamp) FROM prices WHERE symbol = ? and series = ? GROUP BY symbol ORDER BY timestamp', (t1, series))
for row in cursor:
    print row
    

##########################################################################
# Now I am writing this data from the database into an Excel spreadsheet
##########################################################################

'''This basically works but one thing that breaks it is how I made the 'date_object' and single
explicit date in the import_rows() above which, I think means that, because they all have the 
same date, reports the last entry in the array with that ticker'''

import xlsxwriter


def createExcelWithDailyPriceMoves(ticker,conn):
    c=conn.cursor()
    cursor = c.execute('SELECT symbol, timestamp, close FROM prices WHERE symbol = ? and series = ? ORDER BY timestamp',(ticker,series))
    
    excelFileName = "/Users/mharbour/python_tests/"+ticker+".xlsx"
    # Create a workbook (it's like opening a file)
    workbook = xlsxwriter.Workbook(excelFileName)
    # Create an empty worksheet
    worksheet = workbook.add_worksheet("Summary")
    # We write the stuff into the worksheet row by row
    worksheet.write_row("A1",["Top Traded Stocks"])
    worksheet.write_row("A2",['Stock','Date','Closing'])
    lineNum = 3
    for row in cursor:
        worksheet.write_row("A"+str(lineNum), list(row))
        print "A"+str(lineNum), list(row)
        lineNum = lineNum + 1
    
    chart1 = workbook.add_chart({ 'type' : 'line' })
    chart1.add_series({'categories' : '=Summary!$B$3:$B$' + str(lineNum),'values' : '=Summary!$C$3:$C$'+str(lineNum)})
    # Add a chart title and some axis labels
    chart1.set_title({'name' : ticker})
    chart1.set_x_axis({'name':'Date'})
    chart1.set_y_axis({'name': 'Closing Price'})
    
    # Insert the chart into the worksheet (with an offset)
    worksheet.insert_chart('F2',chart1,{'x_offset' : 25, 'y_offset' : 10})
    workbook.close()
    
# Create a connection

conn=sqlite3.connect('example.db')
# c=conn.cursor()
# c.execute('CREATE TABLE prices (SYMBOL text, SERIES text, OPEN real, HIGH real, LOW real, CLOSE real, LAST real, PREVCLOSE real, TOTTRDQTY real, TOTTRDVAL real, TIMESTAMP date, TOTALTRADES real, ISIN text, PRIMARY KEY (SYMBOL, SERIES, TIMESTAMP))')
# conn.commit()

createExcelWithDailyPriceMoves('IIFLFIN',conn)
#close the connection

