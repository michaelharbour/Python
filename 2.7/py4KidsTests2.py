'''It seems that I hadn't uploaded the latest python_tests directory to drive
   when packing my machine up for Atlanta so I was missing some of the later
   chapter examples.  Thus I created part2 of the file and started with chapter
   12 (Tkinter) - I was midway through but had taken some time off so restarted
   to refresh.
'''

## CHAPTER 12 - USING TKINTER FOR BETTER GRAPHICS


# def hello():
#     print('Hello there!')

# from Tkinter import *
# tk = Tk()
# btn = Button(tk, text='click me', command=hello())
# btn.pack()

# tk.mainloop()

# import turtle
# t = turtle.Pen()

# def person(width,height):
#     print('I am %s feet wide, %s feet hight.' % (width, height))

# # person(4,3)
# person(height=3, width=4)

## Creating a canvass

# from Tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# canvas.create_line(0,0,500,500)

# tk.mainloop()

## Doign the same thing with Turtle

# import turtle
# turtle.setup(width=500, height=500)
# t = turtle.Pen()
# t.up()
# t.goto(-250,250)
# t.down()
# t.goto(500,-500)

# '''Not sure why this isn't drawing - must be a 2.7 vs. 3.0 thing'''

## Drawing boxes

# from Tkinter import *
# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()
# canvas.create_rectangle(10,10,50,50)

# tk.mainloop()

## Drawing lots of  and with color

# from Tkinter import *
# import random

# def random_rectangle(width, height, fill_color):
#     x1 = random.randrange(width)
#     y1 = random.randrange(height)
#     x2 = x1 + random.randrange(width)
#     y2 = y1 + random.randrange(height)
#     canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color)

# tk = Tk()
# canvas = Canvas(tk, width=400, height=400)
# canvas.pack()

# # rand_color = ['green', 'red', 'blue', 'orange', 'yellow', 'pink', 'purple', 'violet', 'magenta', 'cyan']
# # my_color = 'red'

# rand_hex_clr = '#f154e1'
# # print(rand_hex_clr)

# for p in range(0,100):
#     # clr = int(random.randrange(10))-1 # This is for an explicit list of colors with known values
#     # my_color = rand_color[clr]

#     r = lambda : random.randint(0,255) # this is a on-the-fly function 
#     rand_hex_clr = ('#%02x%02x%02x' % (r(),r(),r()))
#     print(rand_hex_clr)

#     random_rectangle(400,400,rand_hex_clr)

# tk.mainloop()


## Using the color chooser function  
 
'''For some reason I could not get this to work on OSX the panel comes up but nothing in it'''

# from Tkinter import *
# from tkColorChooser import askcolor
# import random

# def getColor():
#     color = askcolor()
#     print color

# Button(text='Select Color', comamnd=getColor()).pack()
# mainloop()


## DRAWING ARCS

from Tkinter import *

# tk = Tk()
# canvas = Canvas(tk, width=500, height=500)
# canvas.pack()
# canvas.create_line(0,0,500,500)

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_arc(10,10,200,100, extent=180, style=ARC)

mainloop()

