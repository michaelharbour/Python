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

'''Here we are using a recursive solution to do the same calculation
RECURSION IS FUNKY!'''

# def my_mult2(a,b):
#     if b == 1:
#         print("I'm in the last loop!")
#         print a
#         return a
#     else:
#         # val = a + my_mult2(a, b-1)
#         print("A is now equal to " + str(a) + ", while b is now equal to " + str(b))
#         return a + my_mult2(a, b-1)
        

# print(my_mult2(5,10))

'''perhaps a bit easier to understand are factorals using recursion.  This is the process in which you want
a factoral of some number (let's say 5), so that means 5*4*3*2*1 (or 120).  We know that our base case in the 
example of factorals are 1! returns 1 and 0! returns 1, so those will be our base conditions'''

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n-1)
 
# print(fact(0))
# print(fact(5))

# Here is a comparison between an interitive solution and a recursive one

# def get_recursive_factoral(n):
#     if n < 0:
#         return -1
#     elif n < 2:
#         return 1
#     else:
#         return n * get_recursive_factoral(n-1)

# def get_iterative_factoral(n):
#     if n < 0:
#         return -1
#     else:
#         fact = 1
#         for i in range(1, n+1):
#             fact *= i
#         return fact

# print(get_recursive_factoral(4))
# print(get_iterative_factoral(4))

'''Use recurussion to draw out the Fibonacci sequence'''

# def fib(n):
#     if n <= 2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# # print(fib(10))

# for i in range(1,10):
#     print(fib(i))

'''palindrome check (is a phrase the same backwards as forwards'''

# def isPalendromes(s):

#     def toChars(s):
#         s = s.lower()
#         ans = ''
#         for c in s:
#             if c in 'abcdefghijklmnopqrstuvwxyz':
#                 ans = ans + c
#         return ans

#     def isPal(s):
#         if len(s) <= 1:
#             return True
#         else:
#             return s[0] == s[-1] and isPal(s[1:-1])
#     return isPal(toChars(s))

# print(isPalendromes('monkey is si yeknom'))

'''using recursion twice to solve moving rings between towers problem
   there are three towers with four disks stacked largest to smallest on one.
      Your challenge is to move them one by one to another tower, never putting
      a larger disk above a smaller one, until they are stacked, largest to smallest
      on the new tower'''

# def printMove(fr, to):
#     print('move from' + str() + ' to ' + str(to))

# def Towers(n, fr, to, spare):
#     if n==1:
#             printMove(fr, to)
#     else:
#         Towers(n-1, fr, spare, to)
#         Towers(1, fr, to, spare)
#         Towers(n-1. spare, to, fr)

#########################################
#  DICTIONARIES
#########################################

# def lyrics_to_frequencies(lyrics):
#     myDict = {}
#     for word in lyrics:
#         if word in myDict:
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
#     return myDict

# she_loves_you = ['she', 'loves', 'you', 'yeah','yeah','yeah','she','loves',
# 'you','yeah','yeah','yeah','You','think',"You've",'lost','your','love']

# def most_common_words(freqs):
#     values = freqs.values()
#     best = max(values)
#     words = []
#     for k in freqs:
#         if freqs[k] == best:
#             words.append(k)
#     return (words, best)

''''This part was intended to walk the frequency dictionary and delete words if they were over the minTimes value,
    append it to your result and print that out. His original script didn't make sense to me, so I commented it out and
    made a simplified check to do the same thing... I think'''

# def words_often(freqs, minTimes):
#     result = []
#     done = False
#     while not done:
#         temp = lyrics_to_frequencies((freqs))
#         print(temp)
#         for myKey in temp.keys():
#             if temp[myKey] >= 2:
#                 result.append(myKey)
#         # if temp[1] >=  minTimes:
#         #     print(temp[0])
#         #     result.append(temp)
#         #     print(result)
#         #     for w in temp[0]:
#         #         del(freqs[w])
#             else:
#                 done = True
#     return result

# print(lyrics_to_frequencies(she_loves_you))

# print(most_common_words(lyrics_to_frequencies(she_loves_you)))

# print(words_often(she_loves_you,5)) 

'''How to do the fibonacci sequence more efficiently than using recursion with a dictionary.  The reason being that we end up calculating
each step every time we run through the recursion.  Not a big deal for 5 steps, but for 1000 steps or 10000, that gets to be a lot of 
redundant calculation'''

# Do a lookup first in case already calculated the value
# modify dictionary as progress through function calls.

# def fib_efficient(n,d):
#     if n in d:
#         return d[n]
#     else:
#         ans = fib_efficient(n-1, d) + fib_efficient(n-2, d) # 'd' seems to denote the key of the dictionary in this context
#         d[n] = ans #this sets the value of n-1 + n-2 to the index (key) in the dictionary before running recursively through the function again
#         return ans

# d = {1:1, 2:2}
# print(fib_efficient(6,d))
# print(d)

#############################################################
# CHAPTER 7 - TESTING, DEBUGGIN, EXCEPTIONS AND ASSERTIONS
#################################################################

'''The 'Try' and 'Except' clauses'''

# a = int(input('tell me a number: ')) # Put a string in here to get the normal exception statement
# b = int(input('Tell me another: '))
# print('a / b = ' + str(a/b))
# print('a + b = ' + str(a+b))

# '''There is probably a more elegant way to limit this to 3 tries.  This is my brute-force method.'''

# n = 1
# while True and n < 4:
#     try:
#         a = int(input('Tell me a number: '))
#         b = int(input('Tell me another number: '))
#         print('a/b = ' + str(a/b))
#     except:
#         if n == 2:
#             print('This is your last chance...')
#         else:
#             print('Bug in user input.  This needs to be a number.')
#             print n
#         n += 1
#         continue

'''You can also get specific with the type of exception:'''

# n = 1
# while True and n < 4:
#     try:
#         a = int(input('Tell me a number: '))
#         b = int(input('Tell me another number: '))
#         print('a/b = ' + str(a/b))
#     except NameError:
#         if n == 2:
#             print('This is your last chance...')
#         else:
#             print('This needs to be a number.  Please try again.')
#             # print n
#         n += 1
#         continue
#     except ZeroDivisionError:
#         if n == 2:
#             print('This is your last chance...')
#         else:
#             print('You cannot divide a number by Zero. Please Try again.')
#             # print n
#         n += 1
#         continue
#     except:  # Catch all for all other exceptions in this case
#         if n == 2:
#             print('This is your last chance...')
#         else:
#             print('Something went wrong. Please try again.')
#             # print n
#         n += 1
#         continue

'''Pretty hacky demostration or raise exception'''

# def get_ratios(L1,L2):
#     '''Assumes: L1 and L2 are lists of equal length of numbers
#     Returns: A list containing L2[i]/L2[i]'''
#     ratios = []

#     for index in range(len(L1)):
#         try:
#             ratios.append(int(L1[index])/int(L2[index]))
#         except ZeroDivisionError:
#             ratios.append(float('nan')) # nan = not a number
#         except:
#             raise ValueError('get_ratios called with bad arg.  This needs to be a number')
#     return ratios

# first_list = []
# second_list = []

# for n in range(3):
#     first_list.append(raw_input('We\'re going to make a list of 3 numbers.  Enter a number:'))
#     n += 1

# for y in range(3):
#     second_list.append(raw_input('Were going to make a list of three more.  Enter a number:'))
#     y += 1

# my_ratios = get_ratios(first_list,second_list)

# for x in range(3):
#     print(my_ratios[x])

'''another example of exceptions'''

# my_class = [[['peter', 'parker'], [80.0, 70.0, 85.0]],[['bruce', 'wayne'], [100.0, 80.0, 74.0]],
#             [['captain', 'america'], [8.0, 10.0, 96.0]],[['deadpool'], []]]

# def get_stats(class_list):
#     new_stats = []
#     for elt in class_list:
#         new_stats.append([elt[0], elt[1], avg(elt[1])])
#     return new_stats

# # def avg(grades):
# #     try:
# #         return sum(grades)/len(grades)
# #     except ZeroDivisionError:

# #         '''Dropping in 0.0 if no grades data is entered'''

# #         print("Warning: no grades data")
# #         return 0.0

# # ALTERNATE USING ASSERTION ERRORS FOR AVG FUNCTION

# def avg(grades):
#     assert not len(grades) == 0, 'No grades data'
#     return sum(grades)/len(grades)

# print(get_stats(my_class))

###############################################################################
#
#   OBJECT ORIENTATED PROGRAMMING - CREATING A CLASS AND INSTANCE OF AN OBJECT
#
###############################################################################

'''Creating a simple coordinate class to show how defining a class and calling an isntance works'''

# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def distance(self, other):
#         x_diff_sq = (self.x-other.x)**2
#         y_diff_sq = (self.y-other.y)**2
#         return (x_diff_sq + y_diff_sq)**0.5

# c = Coordinate(3,4)
# # origin = Coordinate(0,0)
# # other_coordinate = Coordinate(1,2)
# # print(c.x)
# # print(origin.x)
# # print(c.distance(origin))

# print(c) 

'''if you don't tell the class what to do with the print statement, it will \
return the name of the class, type and hex of the memory address'''

# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return("The following object is an instance of the 'Coordinate' class.\n  Pos.x, Pos.y = " + str(self.x) + "," + str(self.y))
#     def distance(self, other):
#         x_diff_sq = (self.x-other.x)**2
#         y_diff_sq = (self.y-other.y)**2
#         return (x_diff_sq + y_diff_sq)**0.5

# c = Coordinate(3,4)

# print(c) 
'''isinstance() is a special method (function), to let you know if an object is an isntance of a class.
There is a another special method called issubclass() that lets you do the same thing for subclasses of something.'''

# print(isinstance(c, Coordinate))

# class Fraction(object):
#     def __init__(self, num, denom):
#         '''Num and denom are intergers'''
#         assert type(num) == int and type(denom) == int
#         self.num = num
#         self.denom = denom
#     def __str__(self):
#         '''returns a string representation of self'''
#         return str(self.num) + "/" + str(self.denom)
#     def __add__(self, other):
#         '''returns a new fraction representing...'''
#         top = self.num * other.denom + self.denom * other.num
#         bott = self.denom * other.denom
#         return Fraction(top,bott)
#     def _sub__(self, other):
#         '''Returns a new fraction representing....'''
#         top = self.num * other.denom - self.denom * other.num
#         bott = self.denom * other.denom
#         return Fraction(top, bott)
#     def __float__(self):
#         '''Returns a flaot value of the fraction'''
#         return self.num/self.denom
#     def inverse(self):
#         '''Returns a new fraction representing...'''
#         return Fraction(self.denom, self.num)

# a = Fraction(1,4)
# b = Fraction(3,4)
# c = a + b # Because these are fraction objects, Python is going to see the '+' symbol and look to see if there is an __add__ override
# print(c) 
# # print(float(c)) # In Python 3.x this should return the same as below, but does not seem to want to swallow the overwritten attribute
# print(float(Fraction.__float__(c))) # This should not need the first 'float' to make this a float.  Some funky 2.7x v 3.x stuff.
# # print(float(b.inverse())) #Also should just be returning the inverse of the fractional pair, but there is some 2.7 int stuff at work here.

###################################
# GETTERS AND SETTERS
###################################

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None
    def get_age(self): # Getter
        return self.age
    def get_name(self):
        return self.name # Getter
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname = ""):
        self.name = newname
    def __str__(self):
        return "animal"+str(self.name)+":"+str(self.age)

a = Animal(3)
print a.get_age()
a.set_name("Tigger")
print(a.get_name())
a.set_age(15)
print(a.get_name() + " has grown old and is now " + str(a.get_age()) + " years old!\n")
