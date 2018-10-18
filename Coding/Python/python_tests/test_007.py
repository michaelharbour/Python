'''This is just a test page to work out python as I go through various exercises'''

###########################
# Assigning values in Python and simple arithmetic
###########################

# usa_gold = 50
# ussr_gold = 24
# romainia_gold = 1
# total_gold = usa_gold + ussr_gold + romainia_gold
# print(total_gold)
# romainia_gold += 1
# print(total_gold)

# hi = 'hello there'
# name = 'michael'
# greet = hi + name
# print (greet)
# greeting = hi + ' ' + name
# print(greeting)
# silly = hi + (" " +name)*3
# print(silly)

##########################
# Adding strings and floats together and some differences in Py 2.7 vs. Py 3.x
##########################

# x = 1
# print(x)
# x_str = str(x)
# print "my fav num is", x, ".", "x =", x
# print("my fav num is " + x_str + ". " + "x = " + x_str)

# Note that in 3+ you can use commas inside the parenthesis to autogenerate spaces, however
# 2.7 will not work this way unless there are no parenthesis.  So, if you wnat to use a multiplier,
# you will need to concatenate.

# name = raw_input('What is your name?\n')
# print("\nHi " + name + "!\n")*5
# num = int(input("Type a number..."))
# print(5*num)

# x = float(input("Enter a number for X: "))
# y = float(input("\nEnter a number for Y: "))

##########################
# if / else statements and while loops
##########################

# if x == y:
#     print("\nX and Y are equal")
#     result = str(int(x/y))
#     if y != 0:
#         print("\nTherefore, X / Y is " + result + "\n")
# elif x < y:
#         print("\nX is smaller.")
# else:
#     print("\nY is smaller.")
# print("\nThanks!")

# n = raw_input('You\'re in the Lost Forest.  Go Left or Right?\n')
# while n.lower() == "right":
#     n = raw_input('\nYou\'re in the Lost Forest.  Go Left or Right?\n')
# print("\nYou got out of the Lost Forest!")

######################
# For loops
######################

# for n in range(10):
#     print(n+1, "\n") #This has been changed to work with Python 3.x syntax (,s inside of brackets as spacing)

# mysum = 0
# for i in range (7,10):
#     mysum += i
# print(mysum)

# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i  
# print(mysum)

################
# String Manipulation
##################

# s = 'Michael Harbour'
# print len(s)
# print s[-1]
# print s[0]
# print s[6:0:-1]
# print s[0:(len(s)+1):-1]
# print s[::-1] # (same as above, but a little macro that doesn't run into the space issue - could be a 2.7 thing)
# s = "hello"
# #s[0] = 'y' # The logic being that you change the string to yellow but strings are immutable in Python and you have to create a new string as below
# s = 'y' + s[1:len(s)+1]
# print(s)

# s = 'MichaelShawnHarbour'
# for index in range(len(s)):
#     if s[index].lower() == 'i' or s[index].lower() == 's':
#         print(s[index].lower())

# for char in s:
#     if char.lower() == 'i' or char.lower() == 's':
#         print('There is an ' + char.lower())

# an_letters = 'aefhilmnorsxAEFHILMNORSX'

# word = raw_input("I will cheer for you!  Enter a word: ")
# times = int(input("Enter your enthusiasm level (1-10): "))

# i = 0
# while i < len(word):
#     char = word[i]
#     if char in an_letters:
#         print("Give me an " + char + "! " + char)
#     else:
#         print("Give me a " + char + "! " + char)
#     i += 1
# print("What does that spell?")
# for i in range(times):
#         print(word + "!!!")

# Doing this in a more Pythonic way

# for char in word:
#     if char in an_letters:
#         print("Give me an " + char + "! " + char)
#     else:
#         print("Give me a " + char + "! " + char)
# print("What does that spell?")
# for i in range(times):
#         print(word + "!!!")
       

######################
# USING ALGORITHMS
######################

# To find the cube root of something (must be an interger)
 
# cube = 8

# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != abs(cube):
#     print(str(cube) + " is not a perfect cube.")
# else:
#     if cube < 0:
#         guess = -guess
#     print('Cube root of ' + str(cube) + ' is ' + str(guess))

# program to find an BRUTE FORCE 'approximate' cube root of something using epsilon (a difference) as a qualifier 
# that an amount is 'good enough'.  Python 2.7 appears to have issues with concatendating strings and 
# integers, so I have used the str() function where necessary.

# cube = 1000
# my_epsilon = 0.001
# guess = 0.0
# increment = 0.0001
# num_guesses = 0

# while abs(guess**3 - cube) >= my_epsilon and guess <= cube:
#     guess += increment
#     num_guesses += 1
#     print(guess + num_guesses)
# print('num_guess = ' + str(num_guesses))
# if abs(guess**3 - cube) >= my_epsilon:
#     print('Failed on cube root of' + str(cube))
# else:
#     print(str(guess) + " is close to the cube root of" + str(cube))

# BISECTION SEARCH TECHNIQUE - look for the cube root by eliminating half of the selections at a time.
# This radically reduces the number of guess that it takes to guess the number.

# cube = 1000
# epsilon = 0.01
# num_guesses = 0
# low = 0
# high = cube
# guess = (high + low)/2.0

# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube :
#         low = guess
#     else:
#         high = guess
#     guess = (high+low)/2.0
#     num_guesses += 1
# print 'num_guesses =' + str(num_guesses)
# print str(guess) + ' is close to the cube root of ' + str(cube)

# low = 1
# high = 1000
# answer = input('Pick a number between ' + str(low) + ' and ' + str(high) + '.  Integers only please: ')
# guess = 500
# div = (high - low)/2.0
# num_guesses = 0

# if answer == 1000:
#     guess = 1000

# while answer <= low-1 or answer >= high+1:
#     answer = input('I said a number  between ' + str(low) + ' and ' + str(high) + '!  Try again: ')

# while guess <= high and guess != answer:
#     print(guess)
#     if guess < answer:
#         low = guess
#     else:
#         high = guess
#     guess = ((high - low)/2)+low  
#     num_guesses += 1

# print('Your number is ' + str(guess))
# print('The number of tries it took me to guess this was ' + str(num_guesses))

#########################
# HOW TO WRITE AND CALL/INVOKE A FUNCTION
#########################

'''Typically functions are organized at the top of a program and called later on in the main body,
but mine are lower here because I am working linearally through the MIT class *this is lesson 4,
so I am treating this like the top of a program'''

def is_even (i): # Here we have the keyword 'def', the name of the function 'is_even' and the number of parameters or args (i)
    '''
    Input: i, a positive int
    Returns True if i is even, otherwise False
    '''
    # This above is called a 'Specification Docstring'
    # Below is called the body.
    # print('Inside is even') # Run some commands
    remainder =  i % 2
    return remainder == 0 # 'return' is the keyword; we add an expression to evaluate and return

#################
# Scope
#################

'''Scope is going to be a 'completely different environment thatn that of the main program', which is essentially binding
a formal prameter to an actual parameter, modifying it in the new environment and mapping that new value back to the original
program'''

# def f(x):
#     x = x+1
#     print('in f(x) : x =' + str(x))
#     return x

# x = 3
# z = f(x)
# print(z)

# def is_even_with_return( i ):
#     '''
#     Input i, a positive int
#     Returns True if i is even, otherwise False
#     '''
#     print('with return')
#     remainder = i % 2
#     return remainder == 0 # Note that no return, will return 'NONE'



# is_even_with_return(3)
# print(is_even_with_return(3) )

print('All numbers between 0 and 20 : even or not')
for i in range(20):
    i +=1
    if is_even(i):
        print(str(i) + ' even')
    else:
        print(str(i) + ' odd')

# Testing bto012 env