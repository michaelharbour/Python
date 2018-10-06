# '''result = 10*350
# # print(result)'''
##Using the triple comma

# fred = '''How do dinosaurs pay their bills?
# with Tyrannosaurus checks!'''

# print(fred)

# silly_string = '''He said, "Aren't, Isn't, Wouldn't, shouldn't"'''
# print(silly_string)

###Of course you can always use the '\' for 'escaping.

# myscore = 1000
# message = 'I scored %s points'
# print(message % myscore)

# joke_text = '%s : a device for finding furniture in the dark'
# bodypart1 = 'knee'
# bodypart2 = 'shin'
# print(joke_text % bodypart1.capitalize())

#formatting 

# spaces = ' ' * 25
# print('%s 12 Butts Wynd' % spaces)
# print('%s Twinklebottom Heath' % spaces)
# print('%s West Snoring' % spaces)
# print('')
# print('')
# print('Dear Sir')
# print('')
# print('I wish to repor that the tiles are missing from the')
# print('outside toilet roof.')
# print('I think it was a bad wind the other night that blew them away')
# print('')
# print('Regards')
# print('Malcolm Dithering')

# print(100 * 'snirt')

# List exercizes

# mammal_employees = ['Evan','Erik','Alex']
# mammal_management = ['Michael','Jim']
# mammal_employees.append('Janice')
# mammal_management.append('Michele')
# # del mammal_employees[3]
# # print(mammal_employees + mammal_management)
# compiled_list = mammal_employees + mammal_management
# compiled_list.remove('Michael')
# print(compiled_list * 5)

# fun with dictionaries

# favorite_colors = {'Zuzu' : 'purple',
#                    'Rosie' : 'pink',
#                    'Ajax' : 'orange',
#                    'Jaxon' : 'green',
#                    'Janglo' : 'blue'
#                    }

# print(favorite_colors['Zuzu'])

#Chapter 3 #1 Favoriates example

# games = ['monopoly','boggle','scrabble']
# foods = ['turkey','carnitas soft tacos','chili spaghetti']
# favorites = games + foods
# print(favorites)

# Chapter 3 exercize 2Ninja battle

# buildings = 3
# ninjas = 25
# tunnels = 2
# samurai = 40
# total = (ninjas * buildings) + (tunnels * samurai)
# print(total)

#Chapter 3 Exercize 3 'Greetings!'

# first_name = 'Michael'
# last_name = 'Harbour'
# statement = 'Hi there, %s %s!' % (first_name, last_name)
# print(statement)

## CHAPTER 4 - TURTLE

## https://docs.python.org/3.1/library/turtle.html

# import turtle

# t = turtle.Pen()
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(50)
# t.right(270)
# t.forward(50)
# t.up()
# t.left(90)
# t.forward(100)
# t.down()
# t.forward(50)
# t.left(90)
# t.forward(50)

# turtle.done()

## CHAPTER 4 - EX. #1 rectangle

# t = turtle.Pen()
# t.forward(100)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(100)
# t.right(270)
# t.forward(50)

# turtle.done()

## CHAPTER 4 - EX. #2 triangle

# '''For this you need to remember SOH CAH TOA
#    take the ratios of the side and then run that
#    through the inverse (sin, cos, tan) arcsine, etc
#    using a calculator and that givse you the angle
#    You need to remember what the opposite, adj and
#    hypotonuse are'''

# t = turtle.Pen()

# t.forward(100)
# t.left(116)
# t.forward(112)
# t.left(127)
# t.forward(112)

# turtle.done()

## CHAPTER 4 - EX. #3 box without corners - I'm using a conditional statement to save work

# t = turtle.Pen()

# t.up()

# x = 1
# while (x < 5) :
#     t.forward(25)
#     t.down()
#     t.forward(50)
#     t.up()
#     t.forward(25)
#     t.left(90)
#     x += 1

# turtle.done()

## CHAPTER 5 CONDITIONAL STATEMENTS

# age = raw_input('What is your age?')
# if age > 20 :
#     print('You\'re too old!')
#     print('''You're probably feeling tired right now...''')
#     print('Why don\'t you go take a nap!')

## CHAPTER 5 - EX. #2 Twinkies

# twinkies = '501'
# int_twinkies = int(twinkies)

# if int_twinkies < 100 :
#     print('Too few!')
# elif int_twinkies > 500 :
#     print('Too many!')
# else :
#     print('Just right.')

# ## CHAPTER 5 - EX. #3 Just the right number

# money = int(raw_input('How much money do you want to put in?'))

# if money > 99 and money < 501 :
#     print('You put in an amount somewhere between $100 and $500.')
# elif money > 999 and money < 5001 :
#     print('You put in an amount between $1000 and $5000.')
# else :
#     print('You put in $%d dollars into the account.' % (money))

# ## CHAPTER 5 - EX. #4 I can fight those ninjas

# ninjas = int(raw_input("How many ninjas are there?"))

# if ninjas > 50 :
#     print('What chu talkin\' about Willus?')
# elif ninjas <= 50 and ninjas > 30 :
#     print('That\'s too many!')
# elif ninjas <= 30 and ninjas > 10 :
#     print('It\'ll be a struggle, but I can take \'em!')
# else :
#     print('I can fight those ninjas.')


## CHAPTER 5 LOOPS

# for x in range(0, 5):
#     print('Hello, World!')

# for x in range(0,5):
#     y = int(x) + 1
#     print('Hello %03d' % (y))

# wizard_list = ['spider legs', 'toe of frog', 'snail tounge', 'bat wing', 'slug butter', 'bear burp']

# for i in wizard_list:
#     print(i)

# hugehairypants = ['huge', 'hairy', 'pants']
# for i in hugehairypants:
#     print(i)
#     for j in hugehairypants:
#         print(j)

# found_coins = 20
# magic_coins = 70
# stolen = 3
# coins = found_coins
# for week in range(1,53):
#     coins = coins + magic_coins - stolen
#     print('Week %s = %s' % (week, coins))

# compond interest rate calculator

# principal = float(raw_input('What is your intial deposit?'))
# rate = float(raw_input('What is your interest rate?  Use a decimal notation please.'))
# result = principal

# for month in range(1,121):
#     result = result + (result * (rate/12))
#     float_result = float(result)
#     print('Month %s = %.02f' % (month, float_result))
#     year = month%12
#     if year == 0 :
#         print('Your annual total is %.02f' % (float_result))

# A basic while loop
# x = 45
# y = 80
# while x < 50 and y < 100:
#     x += 1
#     y += 1
#     print (x, y)

# basic example of the break command

# x = 100
# while x < 200 :
#     x += 1
#     print(x)
#     if x == 150 :
#         break

# ## CHAPTER 6 PROGRAMMING PUZZLES 

# ## CHAPTER 6 PROGRAMMING PUZZLES - EX. #1 THE HELLO LOOP

# for x in range (0,20):
#     print('Hello %s' % x)
#     if x < 9 :
#         break

# ## CHAPTER 6 PROGRAMMING PUZZLES - EX. #2Even Numbers

# age = int(raw_input('What is your age?'))

# if age%2 == 0 :
#     for x in range (0,120,2):
#         print(x)
#         if x >= age:
#             break
# else :
#     for x in range (1,121,2):
#         print(x)
#         if x >= age:
#             break

# ## CHAPTER 6 PROGRAMMING PUZZLES - EX. #3 My FIVE FAVORITE INGREDIENTS

# ingredients = ['snails', 'leeches', 'gorilla belly-button lint', 'caterpillar eyebrows', 'centipede toes']

# y = 1 
# for x in ingredients:
#     print('%d %s' % (y,x))
#     y += 1

# ## CHAPTER 6 PROGRAMMING PUZZLES - EX. #4 YOUR WEIGHT ON THE MOON

# weight = 225
# for x in range (1,16):
#     moon_weight = weight * .165
#     print('Year %d : Your weight on Earth, %d lbs, would be %d lbs on the Moon.' % (x,weight,moon_weight))
#     weight += 5



## CHAPTER 7 RECYCLING CODE WITH FUNCTIONS AND MODULES

##Using a list function

# tmp = list(range(1,20))
# for i in tmp :
#     print(i)

## Creating a basic function

# def testfunc(firstname, lastname):
#     print('Hello, %s %s' % (firstname,lastname))
    
# first = raw_input('What is your first name?')
# last = raw_input('What is your last name?')

# testfunc(first, last)

## Creating a function to calculate something - net cash in this case

# def savings(pocket_money, paper_route, spending):
#     return pocket_money + paper_route - spending

# cash = float(raw_input('How much money do you have now?'))
# salary = float(raw_input('How much money did you earn on your paper route?'))
# cost = float(raw_input('How much money do you plan to spend?'))

# total = (savings(cash, salary, cost))

# print('That will leave you with $%.02f dollars' % total)

## Variables and Scope - note how, even though you can't use variables from in the function on the 
## outside, you can use variables from outside the function within.

# another_variable = 100

# def variable_test2():
#     first_variable = 10
#     second_variable = 20
#     return first_variable * second_variable * another_variable

# print(variable_test2())

## Another calculator for a task that takes user input (building a spaceship)

# def spaceship_building(cans) :
#     total_cans = 0
#     year = 0
#     print(' ')
#     for week in range(1,5000) :
#         total_cans = total_cans + int(cans)
#         print('Week %s = %s cans' % (week, total_cans))
#         if total_cans >= 5000 :
#             break
#         elif week%52 == 0 :
#             year += 1
#             if year == 1 :
#                 print('That\'s %d year, my friend!' % year)
#             else :
#                 print('That\'s %d years, my friend!' % year)

# print('\n\nIt takes 5000 flattened cans to build a spaceship, my friend.\n')
# num_cans = raw_input('How many cans can you flatten in a week?\n')

# spaceship_building(num_cans)

## Time module

# import time

# print(time.asctime())

## using the sys module and readline function to get user input vs. using raw_input

# import sys

# print(sys.stdin.readline())

# import sys

# def silly_joke():
#     if age >= 10 and age <= 13:
#         print('What is 13 + 49 + 84 + 155 + 97?  A headache.')
#     else :
#         print('Huh?')

# print('What is your age, dude?')
# input_age = sys.stdin.readline()
# age = int(input_age)

# silly_joke()

# ## CHAPTER 7 PROGRAMMING PUZZLES - EX. #1, #2, #3 BAISC MOON WEIGHT FUNCTION

# def moon_weight() :
#     earth_weight = float(raw_input('What is your current weight her on Earth?\n'))
#     weight_gain = float(raw_input('How much weight will you gain each year?\n'))
#     gravity_multiplier = float(raw_input('What is the percentage of Earth\'s gravity on the moon?  In decimal for please...\n'))
#     years = int(raw_input('How many years are you planing to live on the moon?\n'))
#     for i in range(1, years + 1) :
#         adj_weight = earth_weight * gravity_multiplier
#         print('In year %d, your Earth weight of %.02f lbs. would be %.02f on the moon.' % (i, earth_weight, adj_weight))
#         earth_weight += weight_gain

# moon_weight()



# ## CHAPTER 8 - OBJECTS AND CLASSES

# import subprocess as sp ## allows you to clear the shell before running an application in the terminal


# # Setting up clases (parent and children) and objects and inital parameters and attributes 

# class Things :
#     pass # a standard placeholder for orginalization purposes

# class Inanimate(Things):
#     pass

# class Animate(Things):
#     pass

# class Sidewalks(Inanimate):
#     pass

# class Animals(Animate):

#     def breath(self):
#         print('Breathing.')

#     def move(self):
#         print('Moving.')

#     def eat_food(self):
#         print('Eating food.')

# class Mammals(Animals):

#     def feed_young_with_milk(self):
#         print('Feeding young.')

# class Giraffes(Mammals):

#     def __init__(self, spots):
#         self.giraffe_spots = spots

#     def eat_leaves_from_trees(self):
#         print('Eating leaves.')

#     def find_food(self) :
#         self.move()
#         print('I\'ve found food')
#         self.eat_food()

#     def dance_a_jig(self):
#         for i in range(0,4):
#             self.move()

## Assigning objects - call on their classes and parent classes functions

# reginald = Giraffes(25) ## the parameter realates to the 'spots' parameter initialized with the __init__ function for Giraffes
# harold = Giraffes(55)

# oswald = Giraffes(25)
# gertrude = Giraffes(33)

## Do stuff with your objects and their class funtions

# sp.call('clear',shell=True) ## This is the subprocess call that will clear the OSX shell before running.

# reginald.move()
# reginald.breath()
# reginald.eat_food()
# reginald.feed_young_with_milk()

# harold.move()

# reginald.eat_leaves_from_trees()

# print('\nHarold is looking for food...')
# harold.find_food()

# print('\nwhile regina loves to dance...')
# reginald.dance_a_jig()

# print('\nGertrude has %d spots, while Oswald has %d.' % (gertrude.giraffe_spots, oswald.giraffe_spots)) # using class variables

## Using classes and objects using Turtle -- This is an example of how we can instance 
## new objects under the class Pen and use it's functions independently.

# import turtle

# avery = turtle.Pen()
# kate = turtle.Pen()
# jacob = turtle.Pen()

# avery.forward(50)
# avery.right(90)
# avery.forward(50)

# kate.left(90)
# kate.forward(100)

# jacob.left(180)
# jacob.forward(80)

# turtle.done() # keeps the window around.


# ## CHAPTER 8 PROGRAMMING PUZZLES - EX. #1, THE GIRAFFE SHUFFLE

# import subprocess as sp ## allows you to clear the shell before running an application in the terminal

# class Mammals():
#     def left_foot_forward(self):
#         print('Left foot forward...')

#     def left_foot_back(self):
#         print('Left foot back...')

#     def right_foot_forward(self):
#         print('Right foot forward...')

#     def right_foot_back(self):
#         print('Right foot back...')

# class Giraffes(Mammals):

#     def __init__(self, spots):
#         self.giraffe_spots = spots

#     def dance(self):
#         self.left_foot_forward()
#         self.left_foot_back()
#         self.right_foot_forward()
#         self.right_foot_back()
#         self.left_foot_back()
#         self.left_foot_forward()

# ## Assigning objects - call on their classes and parent classes functions

# reginald = Giraffes(25) ## the parameter realates to the 'spots' parameter initialized with the __init__ function for Giraffes


# ## Do stuff with your objects and their class funtions

# sp.call('clear',shell=True) ## This is the subprocess call that will clear the OSX shell before running.


# print('\nwhile Reginald loves to dance...\n')
# reginald.dance()

# ## CHAPTER 8 PROGRAMMING PUZZLES - EX. #2, TURTLE PITCHFORK

# import turtle

# all = ['one', 'two', 'three', 'four']

# for i in all:
#     if i == 'one':
#         i = turtle.Pen()
#         i.forward(150)
#         i.left(90)
#         i.forward(100)
#         i.right(90)
#         i.forward(50)

#     if i == 'two':
#         i = turtle.Pen()
#         i.forward(150)
#         i.left(90)
#         i.forward(50)
#         i.right(90)
#         i.forward(35)

#     if i == 'three':
#         i = turtle.Pen()
#         i.forward(150)
#         i.right(90)
#         i.forward(100)
#         i.left(90)
#         i.forward(50)

#     if i == 'four':
#         i = turtle.Pen()
#         i.forward(150)
#         i.right(90)
#         i.forward(50)
#         i.left(90)
#         i.forward(35)

# turtle.done()



## CHAPTER 9 - BUILT IN FUNCTIONS

# # absolute Value

# e = -10
# print(abs(e))

#####

# steps = -3

# if abs(steps) > 0:
#     print('Character is moving.')

# booleans - return true (1) or false (0)

# mysillylist = []
# print(bool(mysillylist))
# mysillylist.append( 2009 )
# print "Updated List : ", mysillylist
# print(bool(mysillylist))

###########

# x = 0
# print(bool(x))
# x = 15.5
# print(bool(x))

#######

# dob = raw_input('What year were you born?\n')

# if bool(dob):
#     print('Thanks.')
# else:
#     print('You will need to enter a year for your date of birth.')



###### USING THE DIR FUNCTION TO LIST AVAILABLE FUNCTION AND CREATE AND WRITE TO A FILE

# import subprocess as sp ## allows you to clear the shell before running an application in the terminal

# ## FUNCTION TO REMOVE INTERNAL FUNCTIONS FROM DIR LISTING

# def clean_print(inp_type, out_file):
#     inp_type = str(inp_type)
#     # print('\nThese are the non \'special functions\' functions available for %s:\n' % inp_type)
#     full_type = dir(inp_type)
#     edited_type = []
#     for i in full_type:
#         if '__' not in i:
#             edited_type.append(i)
#     # print(edited_type)
#     output_file = open(out_file, 'a')
#     output_file.write('\n\n\nThese are the non \'special functions\' functions available for %s:\n\n' % inp_type)
#     for j in edited_type:
#         output_file.write(' %s' % j)

# ## CREATE EXAPLES OF TYPES OF OBJECTS TO CHECK FOR AVAILABLE FUNCTIONS

# ## USER INPUT

# my_dict = {'one' : 1, 'two' : 2}
# my_list = ['test']
# my_string = 'one'
# my_int = 18
# my_float = 3.14
# my_file = '/Users/mharbour/python_tests/dir_function_printout.txt'

# output_file = open(my_file, 'w+') # this creates the file that the function appends to later on.

# list_to_check = ['my_dict', 'my_list', 'my_string', 'my_int', 'my_float']

# ## DO THE WORK

# sp.call('clear',shell=True) ## clears terminal before printing out functions

# for x in list_to_check:
#     clean_print(x, my_file)
# print('To see the list of functions available for your various types, please open: %s\n' % my_file)


## THE EVAL FUNCTION

# your_calculation = raw_input('Enter an equation (in a pythonic style) and I will s-it out the answer!\n')
# print('%s, that is your answer!' % eval(your_calculation))

## THE EXEC FUNCTION - crazy example of syntax, but it seems to work

# my_small_program = '''print('Ham')
# print('Sandwich')'''

# exec(my_small_program)

# ## FLOATS, INTEGERS, LEN FUNCTION, MIN AND MAX AND RANGE 

# import subprocess as sp

# sp.call('clear',shell=True)

# num = 11
# print('\n\nOriginal number %d' % num)
# fnum = float(num)
# print('Now, using the float function to convert and print out as a 2-pad float number, %.02f' % fnum)

# # However, please note that you can't convert a string that is a float '12.635' 
# # directly into an int.  You have to do a float conversion first.

# inum = int(fnum)
# print('Now, using the int function to convert the float back into an integer. %d' % inum)

# # using the float or int compand to do comparisons on user input data

# age = raw_input('\nWhat is your age?\n')
# age = float(age)
# if age > 11:
#     print('You are %s years to old!' % (age - 11))

# len with return the number of characters in a string or items in a list or pairs in a dict (map)

# test_str = 'Michael Harbour'
# print('\nThe string %s has %d characters' % (test_str,len(test_str)))
# creature_list = ['Ghouls', 'Goblins', 'Spooks', 'Spectres']
# print('\nThe list %s has %d items in it.' % (creature_list, len(creature_list)))
# enemies_dict = {
#                 'Batman' : 'Joker',
#                 'Superman' : 'Lex Luthor', 
#                 'Spiderman' : 'Green Goblin'
#                 }
# print('\nThe dictionary (map) %s has %d item-pairs in it.\n' % (enemies_dict,(len(enemies_dict))))

# fruit = ['banana', 'apple', 'pear', 'orange', 'pineapple']

# for i in range(0,len(fruit)):
#     print('The fruit listed at index %d is %s' % (i,fruit[i]))
# print('There are %d fruits in total' % len(fruit))

# The min and max functions

# numbers = []
# print('Enter in some numbers, hitting return after each.  Hit return without entering anything when you are done.\n')
# while True:
#     new_num = raw_input()
#     if new_num == '':
#         break
#     else:
#         numbers.append(float(new_num))

# print(numbers)


# print('\nThe smallest number in your list is: %s' % min(numbers))
# print('\nThe largest number in your list is: %s\n' % max(numbers))

# print('You can also do this for strings (know that lowercase letters are listed as after uppercase):\n')

# test = 'supercalifragilisticexpialdocious'
# print('The min (closest to the start of the alphabet) in the word %s is %s, and the max is %s' % (test, min(test), max(test)))


# WHOEVER GUESSES THE CLOSEST NUMBER WINS

# from random import randint

## I am not using classes here but want to at some point.

# class Games():
#     pass

# class Players():
#     pass
 
# print('Are you ready to play the guessing game?')
# print('Guess a number between 1 and 100.  Whoever is closest wins!\n')


# player_num = int(raw_input('How many players?'))
# player_guesses = []
# norm_guesses = []
# number = randint(1,100)

# for i in range(0, player_num):
#     while True:
#         guess = raw_input('\nPlayer %s, what is your guess?\n' % (i + 1))
#         if guess in player_guesses: # Guess again if someone has already guessed the same number
#             print('I\'m sorry.  Someone already guessed that number.  Try another:\n')
#             continue
#         else:
#             player_guesses.append(guess)
#             norm_guess = abs(number - int(guess))
#             norm_guesses.append(norm_guess)
#             break

# winning_ans = min(norm_guesses)
# count = 1

# for j in norm_guesses:
#     if j == winning_ans:
#         print('Conratulations player %d, you are our winner! The correct number was %d' % (count, number))
#         break
#     else:
#         count += 1

## Ranges

# print(list(range(0,5))) # They can be used to generate ranges for lists as well
# for i in range(0,25):
#     print('test.%04d.exr' % i) #Here's your basic vfx syntax

# ## Count by twos

# for i in range(0,25,2):
#     print('test.%04d.exr' % i) 

# ## Countdown by twos

# for i in range(24,-1,-2):
#     print('test.%04d.exr' % i)

## creating a file


# ## CHAPTER 9 PROGRAMMING PUZZLES - EX. #1, ABS NUMBERS

# a = abs(10) + abs(-10)

# while True:
#     guess = raw_input('What will the answer of the following equation be: abs(10) + abs(-10)?\n')
#     if int(guess) == a:
#         print('You\'re right!  The correct answer is %d!\n' % a)
#         break
#     else:
#         print('Nope.  Try again!\n')

# b = abs(-10) + -10

# while True:
#     guess = raw_input('Now, what will the answer of the following equation be: abs(-10) + -10?\n')
#     if int(guess) == b:
#         print('You\'re right!  The correct answer is %d!\n' % b)
#         break
#     else:
#         print('Nope.  Try again!\n')



# ## CHAPTER 9 PROGRAMMING PUZZLES - EX. #2, DIR EXERCIZE

# import subprocess as sp

# sp.call('clear', shell=True)

# my_string = 'This is if you not are a reading very this good then way you to have hide done a it message wrong'

# # for e in dir(my_string): # Go through the available functions
# #     if '__' not in e:
# #         print(e)

# # printing the help function via a loop of the dir output was not doable for me at this point so I Just
# # looked for the most promising one (split) and manually ran the help()
# my_array = my_string.split(' ')

# # for i in range(0,len(my_array),2):
# #     print(my_array[i])

# ## CHAPTER 9 PROGRAMMING PUZZLES - EX. #3, COPY FUNCTION

# my_path = '/Users/mharbour/python_tests/'

# orig_file = open(my_path + 'orig_file.txt', 'w+')
# orig_file.write('This is the text from the original file I created!')
# orig_file.close()

# orig_file = open(my_path + 'orig_file.txt', 'r')
# orig_contents = orig_file.read()
# orig_file.close()

# copied_file = open(my_path + 'copy_file.txt', 'w+')
# copied_file.write(orig_contents)
# copied_file.close()



## CHAPTER 10 - USEFUL MODULES

## THE COPY MODULE
# import subprocess as sp
# import copy

# sp.call('clear',shell=True)

# class Animal():
#     def __init__(self, species, number_of_legs, color):
#         self.species = species
#         self.number_of_legs = number_of_legs
#         self.color = color

# harry = Animal('hippogriff', 6, 'pink')
# harriet = copy.copy(harry)

# # print(harry.species)
# # print(harriet.species)

# carrie = Animal('chimera', 4, 'green polka dots')
# billy = Animal('bogill', 0, 'paisley')

# my_animals = [harry, carrie, billy]
# more_animals = copy.copy(my_animals)
# # attr_list = [species, number_of_legs, color]
# for i in range(0,len(more_animals)):
#     print(more_animals[i].species)
#     print(more_animals[i].number_of_legs)
#     print(more_animals[i].color)

# print('\n\nNow, to demonstrate the concept of a shallow copy, we will modify the first list to see what changes\n')

# my_animals[0].species = 'ghoul' # Because it is a shallow copy, the 2nd list isn't actually copying the objects inside

# print('Here is the species of the first animal in my_animals: %s' % my_animals[0].species)
# print('Here is the species of the first animal in more_animals: %s' % more_animals[0].species)

# sally = Animal('sphinx', 4, 'sand')
# my_animals.append(sally)
# print('\nI have appended one animal to the original list so that it now contains %d' % len(my_animals))
# print('But notice that the number of animals in the copied list remains the same: %d' % len(more_animals))

# print('\nSo a shallow copy maintains links to the original objects, but doesn\'t create a new link when a new object is added to the original')

# deep_animals = copy.deepcopy(my_animals) # This should copy the objects as well so modificatoin of the original won't change everything.

# my_animals[0].species = 'zombie'

# print('\nI changed Harry in my first list to now be a %s, and noticed that Harry is the same for the \'copied\' list: %s,\
#  but not for the \'deepcopied\' list: %s\n' \
#  % (my_animals[0].species, more_animals[0].species, deep_animals[0].species))


# The Keyword module

# import keyword
# import subprocess as sp
# sp.call('clear', shell=True)

# print(keyword.iskeyword('if'))
# print(keyword.iskeyword('ozwald'))

# for each in keyword.kwlist:
#     print each

# THE RANDOM MODULE

# import random
# import subprocess as sp
# sp.call('clear', shell=True)

# # print(random.randint(1,100))
# # print(random.randint(100,1000))
# # print(random.randint(1000,5000))

# # num = random.randint(1,100)
# # while True:
# #     print('Guess a number between 1 and 100')
# #     guess = raw_input()
# #     i = int(guess)
# #     if i == num:
# #         print('You guessed right!')
# #         break
# #     elif i < num:
# #         print('Try higher.')
# #     elif i > num:
# #         print('Try lower')

# desserts = ['brownies', 'cookies', 'cake', 'pie', 'fudge','candy']
# print('You get %s.' % random.choice(desserts))

# print('The list, as written, would be in the following order:\n%s\n' % desserts)
# shuffle_desserts = []
# random.shuffle(desserts) #This is odd - I cannot use this function to assign to a new list directly but have to shuffle the existing list and do through a for loop.
# for item in desserts:
#     shuffle_desserts.append(item)
# print(shuffle_desserts)

# # print('However, I use the magic random.shuffle function and, voila:\n%s\nIt\'s now in a different order...' % shuffled_desserts)


## The SYS MODULE

# import sys
# import subprocess as sp
# sp.call('clear', shell=True)

# #STDIN and STDOUT

# # print('Type something in here:')
# # v = sys.stdin.readline() # You can put a number in the parenthesis to limit the number of characters that can be input.
# # print('This is what you typed: %s' % v)

# # sys.stdout.write('The stdout is a lot like the print function but it is an object and has some different features\n')

# # Python Version

# # print(sys.version)

# ## TIME MODULE

# import time

# # print(time.time()) # This actually prints the number of seconds since January 1, 1970 at midnight

# # def lots_of_numbers(max):
# #     t1 = time.time()
# #     for x in range(0, max):
# #         print(x)
# #     t2 = time.time()
# #     print('It took %s second' % (t2-t1))

# # num_inp = raw_input('How many numbers do you want to count to?\n')
# # lots_of_numbers(int(num_inp))

# # print(time.asctime()) # prints out the date in a more readable format

# # t = (2017, 2, 14, 14, 18, 0, 1, 0, 0) # tuple format for time import [year, mo, day, hr., minute, sec, day of week - 0 = mon, day of year, daylight savings boolean)]

# # print(time.asctime(t)) # we can now feed this into asctime and get a properly formated date

# # print(time.localtime()) # prints out time as an object wiht attributes assigned the same data as asctime in approx the same format

# # for item in time.localtime():
# #     print(item)

# # my_time = time.localtime()

# # my_months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

# # print('\nOne way to play with localtime is to break the tuple up by index so you can do things like: %s %s, %s' % (my_months[t[1]-1],t[2],t[0]))

# for x in range(1,61):
#     print(x)
#     time.sleep(1) # sits for one second before proceeding

## USING THE PICKLE MODULE

# import subprocess as sp
# import pickle

# sp.call('clear', shell=True)

# game_data = {
#     'player-position' : 'N23 E45',
#     'pockets' : ['keys', 'pocket knife', 'polished stone'],
#     'backpack' : ['rope', 'hammer', 'apple'],
#     'money' : 158.50
# }

# save_file = open('save.dat','wb')
# pickle.dump(game_data, save_file)
# save_file.close()

# load_file = open('save.dat', 'rb')
# loaded_game_data = pickle.load(load_file)
# load_file.close()

# print(loaded_game_data)


# ## CHAPTER 10 PROGRAMMING PUZZLES - EX. #1, COPIED CARS

# import copy

# class Car:
#     pass

# car1 = Car()
# car1.wheels = 4
# car2 = car1
# car2.wheels = 3
# print(car1.wheels)

# car3 = copy.copy(car1)
# car3.wheels = 6
# print(car1.wheels)

# print(car2.wheels)
# print(car3.wheels)

# # ## CHAPTER 10 PROGRAMMING PUZZLES - EX. #2, FAVORITE THINGS


# import subprocess as sp
# import pickle
# import sys

# sp.call('clear', shell=True)

# favorite_things = {
#     'kids' : ['Janglo', 'Jaxon', 'Ajax', 'Rosie', 'Zuzu'],
#     'wife' : 'Ariella',
#     'places to eat' : 'Chano\'s',
#     'sports teams' : ['Lakers', 'Dodgers']
#  }

# saved_file = open('favorites.dat', 'wb')
# pickle.dump(favorite_things, saved_file)
# saved_file.close()

# load_file = open('favorites.dat', 'rb')
# load_favorite_things = pickle.load(load_file)
# load_file.close()

# # print(type(load_favorite_things))

# # print(load_favorite_things)



# for key, value in load_favorite_things.iteritems():
#     sys.stdout.flush
#     sys.stdout.write(key + ':\t\t') # I am using the sys.write command because I don't want the newline at the end.
#     if isinstance(value, basestring):
#         sys.stdout.write(value) # I would need to figure out a way to standardize the colum spacing to make this look better.
#     else:
#         for val in value:
#             sys.stdout.write(val + ', ')
#     print('\n')





## CHAPTER 11 - MORE TURTLE GRAPHICS

# import turtle
# t = turtle.Pen()

# t.reset()

# for x in range(1,5):
#     t.forward(50)
#     t.right(90)

# for x in range(1,9):
#     t.forward(100)
#     t.left(225)

# for x in range(1,38):
#     t.forward(100)
#     t.left(175)

# for x in range(1,20):
#     t.forward(100)
#     t.left(95)

# for x in range(1,360):
#     t.forward(100)
#     t.left(91)

# for x in range(1,19):
#     t.forward(100)
#     if x % 2 == 0:
#         t.left(175)
#     else:
#         t.left(225)

# for x in range(1,90):
#     t.forward(100)
#     if x % 2 == 0:
#         t.left(178)
#     else:
#         t.left(178)

## Drawing a car

## chassis

# t.color(1,0,0)
# t.begin_fill()
# t.forward(100)
# t.left(90)
# t.forward(20)
# t.left(90)
# t.forward(20)
# t.right(90)
# t.forward(20)
# t.left(90)
# t.forward(60)
# t.left(90)
# t.forward(20)
# t.right(90)
# t.forward(20)
# t.left(90)
# t.forward(20)
# t.end_fill()

# ## first wheel

# t.color(0,0,0)
# t.up()
# t.forward(10)
# t.down()
# t.begin_fill()
# t.circle(10)
# t.end_fill()

# ## second wheel

# t.setheading(0)
# t.up()
# t.forward(90)
# t.right(90)
# t.forward(10)
# t.setheading(0)
# t.begin_fill()
# t.down()
# t.circle(10)
# t.end_fill()


## filling in a circle

# t.color(1,1,0)
# t.begin_fill()
# t.circle(50)
# t.end_fill()

## Making some functions to make painting a little easier

# def mycircle(red, green, blue):
#     t.color(red,green,blue)
#     t.begin_fill()
#     t.circle(50)
#     t.end_fill()


# mycircle(0,.5,0)    # make a green circle

# def mysquare(size, red, green, blue):
#     t.color(red,green,blue)
#     for x in range(1,5):
#         t.forward(size)
#         t.left(90)

# # mysquare(50, 1,.5,.2)       

# red = 1
# green = 0
# blue = 0
# size = 10

# for i in range(1,15):
#     mysquare(size,red,green,blue)
#     size += 10

# t.left(90)

# red = 0
# green = 1
# size = 10

# for i in range(1,15):
#     mysquare(size,red,green,blue)
#     size += 10

# t.left(90)

# green = 0
# blue = 1
# size = 10

# for i in range(1,15):
#     mysquare(size,red,green,blue)
#     size += 10

# t.left(90)

# red =  .5
# green = .5
# blue = 0
# size = 10

# for i in range(1,15):
#     mysquare(size,red,green,blue)
#     size += 10

## using conditionals to choose whether to fill in an object or not.abs

# def mysquare(size, filled):
#     if filled == True:
#         t.begin_fill()
#     for x in range(1,5):
#         t.forward(size)
#         t.left(90)
#     if filled == True:
#         t.end_fill()

# mysquare(150, 1) # Can also just put 'True' in there as well.

# def mystar(size, langle, langle2, filled):
#     if filled == True:
#         t.begin_fill()
#     for x in range(1, 19):
#         t.forward(size)
#         if x % 2 == 0:
#             t.left(langle)
#         else:
#             t.left(langle2)
#     if filled == True:
#         t.end_fill()

# t.color(0.9,0.75,0)
# mystar(75,175,225,1)

# t.color(0,0,0) # Outline
# mystar(75,175,225,0)


# turtle.done()


## CHAPTER 11 - PROGRAMMING PUZZLES - #1 & #2 DRAW AN OCTOGON

# import turtle
# t = turtle.Pen()

# t.reset()

# def dr_octogon(size, fill):
#     if fill == True:
#         t.begin_fill()

#     for each in range(1,9):
#         t.forward((size/2))
#         t.left(45)

#     if fill == True:
#         t.end_fill()

# t.color(1,1,0)
# dr_octogon(100, True)

# t.color(0,0,0)
# dr_octogon(100, False)

# turtle.done()

## CHAPTER 11 - PROGRAMMING PUZZLES - #3 ANOTHER STAR DRAWING FUNCTION

# import turtle
# t = turtle.Pen()

# t.reset()

# def draw_star(size, points):
#     t.pendown()

#     point_range = (points * 2) + 1 # Need to add 1 to complete the ray
#     diff = 360 / int(points) # All angles of the interior rays should add up to 180 degrees
#     return_angle = 180 - ((diff ) / 2) # So diff is for 360 degress.  We take half that to get 180 degrees
#     out_angle = return_angle - (diff) # We use the full diff her for the out rays  !!!  This isn't right in all cases*
#     for i in range(1,point_range):
        
#         t.forward(size)

#         if i % 2 == 1:
#             t.left(return_angle)
#         else:
#             t.right(out_angle)

# t.color(1,0,0)
# draw_star(75,12) #*As the number of points get higher it becomes clear that the math isn't quite right.  Need to investigate


# turtle.done()




## CHAPTER 12 - TKINTER!

from Tkinter import *
import tkMessageBox
import random

# def hello():
#     print('Hello there!')

# tk = Tk()
# btn = Button(tk, text = 'click me', command=hello)
# btn.pack()

# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()

# canvas.create_line(0,0, 500,500)

# ## How to do the canvas and line in turtle - notice the speed difference

# import turtle
# turtle.setup(width=500, height=500)
# t = turtle.Pen()
# t.up()
# t.goto(-250,250)
# t.down()
# t.goto(500, -500)

# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()

## gnerating procedural squares

# def random_rectangle(width, height, fill_color):
#     x1 = random.randrange(width)
#     y1 = random.randrange(height)
#     x2 = x1 + random.randrange(width)
#     y2 = y1 + random.randrange(height)
#     canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
# for x in range(0,100):
#     r = lambda: random.randint(0,255)
#     hex_random_color = ('#%02x%02x%02x' % (r(),r(),r()))
#     random_rectangle(400,400, hex_random_color)


## How to add a color picker to your Tkinter pane

tk = Tk()

from tkColorChooser import askcolor

def getColor():
    color = askcolor() 
    return color

my_color = Button(text='Select Color', command=getColor).pack()

print(my_color)

mainloop()