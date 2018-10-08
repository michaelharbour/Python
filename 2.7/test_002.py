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
# 

king_name = raw_input("You my noble lord!  I have dire news!!  What ist thy name?\n\n")

num_jewels = raw_input("\nHey " + king_name + "!\nHow many jewels were there?\n\n")

jewel_value = raw_input("\nWell " + king_name + ", How much did each jewel cost?\n\n")

total_amount = int(jewel_value) * int(num_jewels)

print "\nOh my goodness!  Those " + num_jewels + " jewels are worth $" + str(total_amount) + " all together!!!\n\n"

dude_names = ["Athos", "Pothos", "Armis"]
dude_ages = [55,34,67]

dude_names.insert(0,"D'Artagan")
dude_ages.append(16)

temp_var = dude_names.pop(0)
dude_names.append(temp_var)

print "There are " + str(len(dude_names)) + " dudes that we are talking about all together.\n\n" +\
       "We've got to put the hurt on someone to put a stop to this."
       
kill = raw_input("Pick a number between 1 and " + str(len(dude_names)) + " and that's the dude we'll off...\n\n")
killOff = (int(kill) - 1)

print "\nGood choice! " + str(dude_names[int(killOff)]) + ", aged " + str(dude_ages[killOff]) + " it is then!\n" +\
      "I will now erase him from the public record....\n\n"
      
del(dude_names[killOff])
del(dude_ages[killOff])

print dude_names
print dude_ages
# print dude_names
# print dude_ages