'''The following are examples from the CS50 (Harvard) 2016 week 8 course on Python, plust some
other examples pulled from various online tutorials, including on building interfaces using
Tkinter'''

# I define main for good programming practices - where I can choose to define functions after they are called
# in the main logic of the program, more like C.

from Tkinter import *
from ttk import Frame, Style
import tkMessageBox

def main():
    
    # Print the first 26 characters of the ascii table (starting with the alphabet).  Use .format
    
#     for i in range(65, 65 + 190):
#         print("{} is {}".format(chr(i),i))

    # Use sys to print the second command line argument (after the program itroot) to screen

#     import sys
#     
#     if len(sys.argv) == 2:
#         print("Hello {}".format(sys.argv[1]))
#     else:
#         print("Hello, world!")
    
    # Print as many arguments as there are after the program to the screen    

#     import sys
# 
#     for i in range(len(sys.argv)):
#         print(sys.argv[i])

    # Print each character of the input arguments to the screen
    
#     import sys
#     
#     for s in sys.argv:
#         for c in s:
#             print(c)
#         print("\n")

    #Use a conditional to print an error and exit(1) to leave the script if num of args not correct (sort of)

#     import sys
#     
#     if len(sys.argv) != 2:
#         print("Missing command line argument!")
#         exit(1)
#     
#     print("Hello, {}".format(sys.argv[1])) 
#     exit(0)     
    
    # Compare to values to show how, unlike C, we are not comparing addresses but the actual values directly
    # Note the difference here from Py 3.x is that print is not a function yet and so, to not print
    # a newline character at the end of the print statment you add a , to denote space rather than newline
    # where as in Py 3.x the syntax is more print("something ", end="")
    
#     print "s:",
#     s = raw_input()
#     print "t:",
#     t = raw_input()
#     
#     if s != None and t != None:
#         if s == t:
#             print("same")
#         else:
#             print("different")

    # Playing with capitalization

#     print "s:",
#     s = raw_input()
#     
#     if s == None :
#         exit(1)
#         
#     t = s.capitalize()
#     
#     print("s: {}".format(s))
#     print("t: {}".format(t))

    # This has to do with the fact that python doesn't allow us access to lower level functions
    # like C such as memory allocation, address assignment, etc. so switching values requires a 
    # workaround at times.  Here is one example

#     x = 1 
#     y = 2
#     
#     print("x is {}".format(x))
#     print("y is {}".format(y))
#     print("Swapping...")
#     # TODO
#     (x,y) = (y,x) # This is an example of tuples
#     print("Swapped...")
#     print("x is {}".format(x))
#     print("y is {}".format(y))

#     from student import Student
#     import csv
# 
#     students = []
#     for i in range(3):
#     
#         print "name:",
#         name = raw_input()
#         
#         print "dorm:",
#         dorm = raw_input()
#         
#         students.append(Student(name, dorm))
#         
# #     for student in students:
# #         print("{} is in {}.".format(student.name, student.dorm))
# 
#     file = open("students.csv", "w")
#     writer = csv.writer(file)
#     for student in students:
#         writer.writerow((student.name, student.dorm))
#     file.close()

   
    '''from Tkinter import * - This has to be put at the module level if using main'''
    
    
    
    '''This is an example of how to use classes and objects to organize your layout and to call
    on your object to bring up your window'''
    
    
    # class michaelsButtons:	 #You must have two empty lines above a class
    
    #     def __init__(root, master): # Master is the same as root in this case
    #         frame = Frame(master)
    #         frame.pack()
            
    #         root.printButton = Button(frame, text="Print Message", command=root.printMessage) # I will have to declare printMessage() later in the script
    #         root.printButton.pack(side=LEFT)
        
    #         root.quitButton = Button(frame, text="Quit", command=frame.quit)
    #         root.quitButton.pack(side=LEFT)
            
    #     def printMessage(root):
    #         print("Wow, this actually worked!")
            

        
    root = Tk()

    # b = michaelsButtons(root) #This is a part of the class example above and needs to be uncommented

    '''Playing with the Entry Widget to retrieve values'''

    ment = StringVar()
    ment2 = StringVar()

    def myReturn():
        mtext = ment.get()
        mtext2 = ment2.get()
        print "Check: {}\n{}\n".format(mtext, mtext2)
        temp = mtext + mtext2
        print temp
        return temp

    def myResult():
        result = "\n" + myReturn()
        print result
        mlabel2 = Label(root, text=result).pack()
        return

    # # Need to investigate Style() some more

    # # Style().configure("TFrame", background="#333", padding=(0, 5, 0, 5), font='serif 10') 

    root.geometry('450x450+1450+100') # The first two numbers
    #                                 # are the size in X&Y and
    #                                 # the second two are the placement on screen

    # frame = Frame(root)
    # frame.pack()
    
    root.configure(background='#494949')

    root.title('Tkinter practice')

    myPad = 3
    myCol = 4
    myRow = 5

    for num in xrange(myCol):
        root.columnconfigure(num, pad=myPad)
        print('root.columnconfigure({:d}, pad={:d})').format(num, myPad)

    for num in xrange(myRow):
        root.rowconfigure(num, pad=myPad)
        print('root.rowconfigure({:d}, pad={:d})').format(num, myPad)

        cls = Button(root, text="Cls")
        cls.grid(row=1, column=0)
        bck = Button(root, text="Back")
        bck.grid(row=1, column=1)
        lbl = Button(root)
        lbl.grid(row=1, column=2)    
        clo = Button(root, text="Close")
        clo.grid(row=1, column=3)        
        sev = Button(root, text="7")
        sev.grid(row=2, column=0)        
        eig = Button(root, text="8")
        eig.grid(row=2, column=1)         
        nin = Button(root, text="9")
        nin.grid(row=2, column=2) 
        div = Button(root, text="/")
        div.grid(row=2, column=3) 
        
        fou = Button(root, text="4")
        fou.grid(row=3, column=0)        
        fiv = Button(root, text="5")
        fiv.grid(row=3, column=1)         
        six = Button(root, text="6")
        six.grid(row=3, column=2) 
        mul = Button(root, text="*")
        mul.grid(row=3, column=3)    
        
        one = Button(root, text="1")
        one.grid(row=4, column=0)        
        two = Button(root, text="2")
        two.grid(row=4, column=1)         
        thr = Button(root, text="3")
        thr.grid(row=4, column=2) 
        mns = Button(root, text="-")
        mns.grid(row=4, column=3)         
        
        zer = Button(root, text="0")
        zer.grid(row=5, column=0)        
        dot = Button(root, text=".")
        dot.grid(row=5, column=1)         
        equ = Button(root, text="=")
        equ.grid(row=5, column=2) 
        pls = Button(root, text="+")
        pls.grid(row=5, column=3)


    # mlabel = Label(root, text='\nUsername',bg='#494949', fg='white').grid(row = 0, column = 0)
    # mEntry = Entry(root, textvariable=ment).grid(row = 0, column = 2)

    # mlabel2 = Label(root, text='\nPassword').grid(row = 2, column = 0)
    # mEntry2 = Entry(root, textvariable=ment2).grid(row = 2, column = 2)

    # mbutton = Button(root, text='Submit', command=myResult, bg='blue')
    # mbutton.grid(row = 3, column = myCol - 2)






    
    
#     '''The basics of loading an image into your window'''
#     
#     photo = PhotoImage(file="icons/polygon.gif")
#     label = Label(root, image=photo)
#     label.pack()

#     '''The basics of creationg a canvas to draw graphics and remove them'''
#     
#     canvas = Canvas(root, width=200, height=100)
#     canvas.pack()
#     
#     blackline = canvas.create_line(0, 0, 200, 50)
#     redline = canvas.create_line(0, 100, 200, 50, fill="red")
#     greenBox = canvas.create_rectangle(5,35,130,65, fill="green") #First two coordinates are your starting point(from the top corner), the second two are where it will end.
# 
#     canvas.delete(redLine) # This allows you to remove graphics should you want to for user input - here it just eliminates what we already did
#     #canvas.delete(ALL) # This would get rid of all the graphics


#     '''The basics of using message box and queries to return feedback'''
#     
#     
#     tkMessageBox.showinfo('Window Title', 'Monkeys can live up to 300 years.')
#     
#     answer = tkMessageBox.askquestion('Question 1', 'Do you like silly faces?')
#     
#     if answer == 'yes':
#         print(' 8===D~ ' )


    
#     '''How to create a basic application layour with a menu and submenus that call functions,
#     A toolbar and a status bar'''
#     
#     def doNothing():
#         print("ok ok I won't...")
#         
#     # ***** Main Menu ******* #
#         
#     menu = Menu(root)
#     root.config(menu=menu)
#     
#     subMenu = Menu(menu)
#     menu.add_cascade(label="File", menu=subMenu)
#     subMenu.add_command(label="Now Project...", command=doNothing)
#     subMenu.add_command(label="Now...", command=doNothing)
#     subMenu.add_separator()
#     subMenu.add_command(label="Exit", command=menu.quit)
#     
#     editMenu = Menu(menu)
#     menu.add_cascade(label="Edit", menu=editMenu)
#     editMenu.add_command(label="Redo", command=doNothing)
#     
#     # ***** Toolbar ******* #
#     
#     toolbar = Frame(root, bg="blue")
#     
#     insertButt = Button(toolbar, text="Insert Image", command=doNothing)
#     insertButt.pack(side=LEFT, padx=2, pady=2)
#     printButt = Button(toolbar, text="Print", command=doNothing)
#     printButt.pack(side=LEFT, padx=2, pady=2)
#     
#     toolbar.pack(side=TOP, fill=X)
#     
#     
#     # ***** Status Bar ******* #
#     
#     status = Label(root, text="Preparing to do nothing.....", bd=1, relief=SUNKEN, anchor=W) # bd is border
#     status.pack(side=BOTTOM, fill=X)
    
    
    
#     '''Using bind to trigger an event using mouse buttons'''
#     
#     def leftClick(event):
#         print("left")
#         
#     def middleClick(event):
#         print("middle")
#         
#     def rightClick(event):
#         print("right")
#         
#     frame = Frame(root, width=300, height=250)
#     frame.bind("<Button-1>", leftClick)
#     frame.bind("<Button-3>", middleClick) #middle and right mouse button are the opposite of what you'd expect
#     frame.bind("<Button-2>", rightClick)
#     frame.pack()
#     
#     '''Using fucntions in your buttons to return values to the terminal'''
#     
#     def printName(event):
#         print("Hello, my name is Bucky!")
#         
#     button_1 = Button(root, text="Print my name")
#     button_1.bind("<Button-1>", printName) # Ties function to button; -1 means left mouse, no () after called functions
#     button_1.pack() 


#     '''Simple log in panel using grid layout - no return values yet except checkbox'''

#     label_1 = Label(root, text="Name", fg="red")
#     label_2 = Label(root, text="Password", fg="red")
#     entry_1 = Entry(root)
#     entry_2 = Entry(root)
#     
#     label_1.grid(row=0, sticky=E) #This is a different syntax - why? - for N,S,E,W alignment
#     label_2.grid(row=1, sticky=E)
#     
#     entry_1.grid(row=0, column=1)
#     entry_2.grid(row=1, column=1)
#     
#     c = Checkbutton(root, text="Keep me logged in")
#     c.grid(columnspan=2)
    
    # '''Using frames to organize your placement'''

    # topFrame = Frame(root)
    # topFrame.pack()
    # bottomFrame = Frame(root)
    # bottomFrame.pack(side=BOTTOM)
    
    # button1 = Button(topFrame, text="Buttton 1", fg="red")
    # button2 = Button(topFrame, text="Buttton 2", fg="green")
    # button3 = Button(topFrame, text="Buttton 3", fg="blue")
    # button4 = Button(bottomFrame, text="Buttton 4", fg="purple")
    
    # button1.pack(side=LEFT)
    # button2.pack(side=LEFT)
    # button3.pack(side=LEFT)
    # button4.pack(side=RIGHT)

# '''using simple alignment commands to stretch your buttons into place'''

    # one = Label(root, text="one", bg="red", fg="white")
    # one.pack()
    # two = Label(root, text="two", bg="green", fg="black")
    # two.pack(fill=X)
    # three = Label(root, text="three", bg="blue", fg="white")
    # three.pack(side=LEFT, fill=Y)

    root.mainloop()

#     '''Working with formatting and the isdigit function to create a simple calculator'''
#     '''This is just a simple accounting program without having been incorporated into Tkinter'''
    
#     hr_rate = raw_input("Please enter your hourly rate: ")
#     if hr_rate[0].isdigit():
#         hr_rate = float(hr_rate)
#     else:
#         hr_rate = float(hr_rate[1:])
#     num_hrs = float(raw_input("Please enter the number of hours worked: "))
#     tax_rate = float(raw_input("Please enter your tax rate: "))
#     real_tax_rate = tax_rate/100
#     gross = hr_rate * num_hrs
#     net = gross - (real_tax_rate * gross)
#     
#     check = tax_rate * gross
#     
#     print('rate = {:.2f}, hours = {:.2f}, tax_rate = {}, gross = {}, taxed amount = {}, net = {}'.format(hr_rate,num_hrs,tax_rate,gross,check,net))
#     
#     print("Your gross salary for the week was: {:.2f}\nAfter taxes your rate was {:.2f}".format(gross, net))
#     
#     
#    
#     
if __name__ == "__main__":
    main()