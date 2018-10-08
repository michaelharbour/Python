'''This is a general test page to jot down basic python scirpts and test
while reading through various documentation, turtorial sites, etc.

adding one additional change'''

# usa_gold = 50
# ussr_gold = 24
# romainia_gold = 1

# total_gold = usa_gold + ussr_gold + romainia_gold
# print(total_gold)

# romainia_gold += 1
# print(total_gold)

# Geek Gurl Fortune Teller Program

import random
import time

print("Welcome to the Fortune teller \n")

question = input("would you like me to tell you your fortune? \n")

time.sleep(2)

fortunes = ['You are a winner' ,
            'A secret admirer will soon send you a sing of affection' ,
            'The one that you love is closer than you thing.' ,
            'Good things will happen to you.' ,
            'You will do great in life' ,
            'If you get a Rasberry Pi, the Geek Gods will shine on you',
            'Don\'t look at me, I am just a computer program and have no mythical powers']

            print(random.choice(fortunes))