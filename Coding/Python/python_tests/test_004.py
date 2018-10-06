import sys
import math


# 
# name = raw_input("What's your name?\n\n" )
# 
# print "Hello " + name +"!\n"
# 
# radius = int(raw_input("How big is the radius of your circle?\n\n"))
# 
# pi = 3.14
# area_of_circle = pi * (radius **2)
# print_area = "\nIf your circle has a radius of " + str(radius) \
#              + ", then the area of your circle would be... " + \
#              str(area_of_circle) + "!\n"
# 
# print print_area
# 
# name_list = [x for x in raw_input("What are the names of your kids?\n\n").split()]
# num = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th", "13th"]
# 
# i = 0
# 
# while i < len(name_list) :
#     print "\nYour " + num[i] + " kid's name is " + name_list[i]
#     i += 1
#     
# #print "\nThe middle kids are " + name_list[1:3] + ", " + name + "."
# middle_kids = [name_list[1:len(name_list)-1]]
# print "\nThe middle kids are... " + str(middle_kids).replace("[['", "").replace("'","").replace("]]","")
# 
##########################################################

##########################################################

# king_name = raw_input("You my noble lord!  I have dire news!!  What ist thy name?\n\n")
# 
# num_jewels = raw_input("\nHey " + king_name + "!\nHow many jewels were there?\n\n")
# 
# jewel_value = raw_input("\nWell " + king_name + ", How much did each jewel cost?\n\n")
# 
# total_amount = int(jewel_value) * int(num_jewels)
# 
# print "\nOh my goodness!  Those " + num_jewels + " jewels are worth $" + str(total_amount) + " all together!!!\n\n"
# 
# dude_names = ["Athos", "Pothos", "Armis"]
# dude_ages = [55,34,67]
# 
# dude_names.insert(0,"D'Artagan")
# dude_ages.append(16)
# 
# temp_var = dude_names.pop(0)
# dude_names.append(temp_var)
# 
# print "There are " + str(len(dude_names)) + " dudes that we are talking about all together.\n\n" +\
#        "We've got to put the hurt on someone to put a stop to this."
#        
# kill = raw_input("Pick a number between 1 and " + str(len(dude_names)) + " and that's the dude we'll off...\n\n")
# killOff = (int(kill) - 1)
# 
# print "\nGood choice! " + str(dude_names[int(killOff)]) + ", aged " + str(dude_ages[killOff]) + " it is then!\n" +\
#       "I will now erase him from the public record....\n\n"
#       
# del(dude_names[killOff])
# del(dude_ages[killOff])
# 
# print dude_names
# print dude_ages
# print dude_names
# print dude_ages


################################################################

################################################################

# 
# emptyVar = {}
# emptyVar['25'] = "Square of negative 5" #make these strings to simplify the user input process
# emptyVar ['3.14'] = "Pi" #This is a float so make this a string as well.
# 
# print "\n\n"
# print emptyVar 
# 
# keyToDel = raw_input("\n\nWhich of these keys do you want to delete?\n\n")
# 
# if keyToDel in emptyVar :
#     print "\nSuccess!\n\n"
#     emptyVar.pop(keyToDel)
#     print "Ok, I've taken out the key-value pair for " + keyToDel + ". See?\n\n"
#     
# print emptyVar


##############################################

# import collections

# dudeNames = ["Athos", "Pothos", "Aramis", "D'Artagnan"]
# 
# for eachName in dudeNames :
# 
#     print "\nThis is a dude, %s.\n" % (eachName)
#     
# print "*******************************************************\n\n"
#     
# mydict = {"guy1" : dudeNames[0], "guy2" : dudeNames[1], "guy3" : dudeNames[2], "guy4" : dudeNames[3]}
# 
# sortedDict = collections.OrderedDict(sorted(mydict.items()))
# 
# 
# x = 0
# 
# endGuy = raw_input("How many guys do you want me to name?  1-4.\n\n")
# 
# for dictKeys in sortedDict.keys():
#     print "\nThis dude, %s, is %s.\n" % (dudeNames[x], dictKeys)
#     if dudeNames[x] == dudeNames[(int(endGuy)-1)] :
#         break
#     x = x+1
#     
# testString = "Now I am going to show off and print out the number of characters in this line. test. TEST. tEst.\n"
# 
# print "\n%s\nThe total number of characters in that line was %d, with padded 0s it would be %04d.\n" \
#       % (testString, len(testString), len(testString))
#       
# print "the first half of this line is:\n\n %s\n\n...whereas the second half is:\n\n%s\n" \
# % (testString[:len(testString)/2-1], testString[len(testString)/2-1:])
# 
# print "The word 'test' appears in the sentence %d times.\n\n" % (testString.lower().count("test"))
# 
# print str(testString.index("test")) + "\n"
# 
# print testString[testString.lower().index("test"):].upper()
# 
# splitString = testString.split(" ")
# 
# print splitString

################################################################################

#stackskills.com Python - Modules are cool for code re-use and after (Our First Serious Program)

import urllib2 # allows us to work with URLs
import traceback

# JC: This is a stupid dummy value. URLs have to be properly formatted
# for urllib2 to eat them: http://www.google.com/

urlToRead = "http://www.google.com" #Just a dummy value to get the while loop going.

crawledWebLinks = {}

#crawledWebLinks["testtwo"] = "test2" #Testing that my print dict statements are working.
#crawledWebLinks["testthree"] = "test3" #Testing tha t my print dict statements are working.


#Initialize and empty directory, in which (key, value) pairs will correspond to (shortname, url) eg ("Google", "https:)

while urlToRead != '': # this actually means "while the next value isn't empty"
    try:
        # JC: Not enough user info here to make this while loop make
        # external sense to them. Let's fix that
        urlToRead = raw_input("Please enter the next URL to read (ex. http://www.google.com/).\nPress enter to stop entering URLs.\n\n")
        if urlToRead == '':
            print "Ok, exiting loop.\n\n"
            break
        # JC: this shortName should be a raw_input and not an input
        # I worry that they're not teaching you good ways to test input
        # and make sure it's not harmful/ it's properly sanitized
        shortName = raw_input("Please enter a shortname for that URL : %s\n\n" % urlToRead)
        webFile = urllib2.urlopen(urlToRead).read()
        crawledWebLinks[shortName] = webFile # this is "webFile and not "webfile"
        continue
    # JC: I do it too, but it's generally a bad idea to just catch all exceptions
    # you need to know *which* exception you're likely to raise in case of an error
    # for urllib2, it's almost always URLError but can be ValueError
    except ValueError as e:
        print "Exception %s trying to parse URL %s.\n(Please try again and make sure it's a full URL.)" % (e, urlToRead)
        traceback.print_exc()
    except urllib2.URLError as e:
        print "Exception %s trying to read from %s. Enter another URL." % (e, urlToRead)
        traceback.print_exc()
        continue
    else:
        print "Cool!  Let's continue!\n\n"
        continue # JC: you misspelled 'continue'

print crawledWebLinks.keys()