'''This is just a test page to work out python as I go through various exercizes'''

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

for n in range(10):
    print(n+1, "\n")

# mysum = 0
# for i in range (7,10):
#     mysum += i
# print(mysum)

# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i  
# print(mysum)