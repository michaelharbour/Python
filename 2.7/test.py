import sys
import math

name = raw_input("What's your name?\n\n" )

print "Hello " + name +"!\n"

radius = int(raw_input("How big is the radius of your circle?\n\n"))

pi = 3.14
area_of_circle = pi * (radius **2)
print_area = "\nIf your circle has a radius of " + str(radius) \
             + ", then the area of your circle would be... " + \
             str(area_of_circle) + "!\n"

print print_area

name_list = [x for x in raw_input("What are the names of your kids?\n\n").split()]
num = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]

i = 0

while i < len(name_list) :
    print "\nYour " + num[i] + " kid's name is " + name_list[i]
    i += 1


