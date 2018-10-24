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

# def is_even (i): # Here we have the keyword 'def', the name of the function 'is_even' and the number of parameters or args (i)
    # This above is called a 'Specification Docstring'
    # Below is called the body.
    # print('Inside is even') # Run some commands
    # remainder =  i % 2
    # return remainder == 0 # 'return' is the keyword; we add an expression to evaluate and return

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

# print('All numbers between 0 and 20 : even or not')
# for i in range(20):
#     i +=1
#     if is_even(i):
#         print(str(i) + ' even')
#     else:
#         print(str(i) + ' odd')

# Testing bto012 env to upload to personal repos

####################################
# TUPLES
####################################


# def get_data(aTuple):
#     nums = ()
#     words = ()
#     for t in aTuple:
#         nums = nums + (t[0],)
#         if t[1] not in words:
#             words = words + (t[1],)
#     min_n = min(nums)
#     max_n = max(nums)
#     unique_words = len(words)
#     return (min_n, max_n, unique_words)

#my_tuple = ((1,"alpha"),(5,"beta"),(10,"gamma"),(17,"gamma"),(-5,"omega"))

# tswift = ((2014, "Katy"),
#           (2014, "harry"),
#           (2012,"Jake"),
#           (2010, "Jake"),
#           (2008, "Joe"))

# (min_year, max_year, num_people) = get_data(tswift)

# print("From " + str(min_year) + " to " + str(max_year) + \
#         ",Taylor Swift wrote songs about " + str(num_people) + " people!")

# print("testing")

####################################
# LISTS
####################################

# total = 0
# L = [1,2,3,4,5,6]

'''adds all the intergers togehter in the list'''

# for i in range (len(L)):
#     total += L[i]
# print(total)

'''same thing, but cleaner and more Pythonic'''

# for i in L:
#     total += i
# print(total)

#########################
# IN LINE FUNCTIONS 
#########################

# L.append(5) #Adds 5 to the end of the list
# print(L)

#########################
# removing items from a list
#############################

'''Use del to remove a specific index from a list
   Use pop to remove the last element of a list
   Use remove to delete the first instance of the search parameter in a list'''

# del(L[0])
# print("I've removed the first item in the list, \n" + str(L))

# L.pop()
# print("Now I've removed the last, \n" + str(L))

# L.remove(3)
# print("Now I've removed 3 from the list, \n" + str(L))

#########################
# TURNING STRINGS INTO LISTS AND VICE VERSA
#############################
# s = "I<3 cs"
# print(s)
# print(list(s))
# print(s.split('<'))

# L = ['a', 'b', 'c']
# print(L)
# print(''.join(L))
# print('_'.join(L))

# L = [9,6,0,3]
# print(L)
# print(sorted(L))
# print(L)
# x = L.sort()
# print(x)
# y = L.reverse() 
# print(y)


#########################
# LISTS ARE MUTABLE AND LINKS CHANGE THE ORIGINAL
#############################

# a = 1
# b = 2
# print(a)
# print(b)

# warm = ['red', 'yellow', 'orange']
# hot = warm
# hot.append('pink')
# print(hot)
# print(warm)

# '''make a copy of a list that won't be linked'''

# cool = ['blue', 'green', 'grey']
# chill = cool[:]
# chill.append('black')
# print(chill)
# print(cool)

# warm = ['red', 'yellow', 'orange']
# sortedwarm = warm.sort()  
# print(warm)
# print(sortedwarm)

# cool = ['grey', 'green', 'blue']
# sortedcool = sorted(cool)
# print(cool)
# print(sortedcool)

# warm = ['yellow', 'orange']
# hot = ['red']
# brightcolors = [warm]
# brightcolors.append(hot)
# print(brightcolors)
# hot.append('pink')
# print(hot)
# print(brightcolors)

'''Using a list copy to work off of so your are not changing the list as you go'''

# def remove_dups (L1,L2):
#     L1_copy = L1[:]
#     for e in L1_copy:
#         if e in L2:
#             L1.remove(e)

# X1 = [1,2,3,4]
# X2 = [1,2,5,6]

# print(X1)
# print(X2)

# remove_dups(X1,X2)

# print(X1)
# print(X2)

'''strings and tuples parse differently so you have to watch them'''

# def always_sunny(t1,t2):
#     '''t1 and t2 are not empty'''
#     sun = ("sunny", "sun") # a tuple
#     first = t1[0] + t2[0]
#     return(sun[0], first)

# print(always_sunny(('cloudy'),('cold',))) #Trick here is that ('cold',), the comma denote that this is a single elem tuple, not a string

# L = ["life", "answer", 42, 0]
# for thing in L:
#     if thing == 0:
#         L[thing] = "universe"
#     elif thing == 42:
#         L[1] = "everything"

# print(L)

'''More on mutating strings'''

# L1 = ["bacon", "eggs"]
# L2 = ["toast", "jam"]
# brunch = L1
# L1.append("juice") # mutates original list so that brunch is now modified as well.
# brunch.extend(L2) # will add the elements of the list to the end, as opposed to the full list which append() would do.
# print(brunch)

#########################
# RECURSION, DICTIONARIES & THE IDEA OF RECURSION
############################

'''Countdowm'''

# i=10
# while(i>0):
#    print i
#    i-=1


'''Here we are creating a silple multiply fuction to show the idea of recursion'''

# def my_mult(a,b):
#     result = 0
#     while b > 0:
#         # print(b)
#         # print(result)
#         result+=int(a)
#         b-=1
#     print(result)

# my_mult(5,10)

'''Here we are using a recursive solution to do the same calculation'''

def my_mult2(a,b):
    if b == 1:
        print("I'm in the first loop!")
        return a
    else:
        print("A is now equal to " + str(a) + ", while b is now equal to " + str(b))
        return a + my_mult2(a, b-1)

print(my_mult2(5,10))
