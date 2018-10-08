import math, sys
# 

while True:
    usrInpt = ""
    usrMlt = ""
    
    try:
        usrInp = float(raw_input("\nWe are going to make a simple calculator.\nPlease enter a number you want multiplied:\t"))
        usrMlt = float(raw_input("\nThank you!  Now please enter what you want to multiply this number by:\t\n"))

        def myCalc(mult1, mult2):
            result = float(usrInp) * float(usrMlt)
            print "%.3f * %.3f = %.3f!  Now you know!\n\n" % (mult1, mult2, result)
            return

        myCalc(usrInp,usrMlt)
        break
    
    except ValueError as e:
        print "Exception %s.  \n\nMake sure you enter a number (and don't spe1l that number out - digits please)!" % e
#         traceback.print_exc()
        continue

myRadius = float(raw_input("Now let's determine the area of a circle.  What is the radius of the circle?\n\n"))
# 
def calcAreaOfCircle(radius):
    pi = 3.15415
    area = pi * (radius ** 2)
    print "If your radius is %.3f, then the area of your circle will be %.3f!\n\n" % (radius,area)
# 
calcAreaOfCircle(myRadius)

print "Man...  You're really getting the hang of this!\n\n"

print "Now I am going to do something amazing.\n" + \
    "Enter a series of radii which you want to use to calculate the area of a circle for" \
    "\n(to finish just hit return without entering a number:\n\n"

radii = []
x = 0

while x != '':
    try:
        x = raw_input()
        radii.append(x)
    except ValueError, e:
        print "Error",e,x
    
print radii

print "Great!  Let's see what the area of those radii will be!\n\n"

for num in xrange(len(radii)-1):
    calcAreaOfCircle(float(radii[num]))
    
print "Now we are going use a python dictionary to record both the area and circumfrence of a circle for each radii you've already given.\n\n"

pi = 3.1415

# area = pi*(r squared)
# circumfrence = 2*pi*r

def recordAreaAndCirc(list):
    areaResult = []
    circResult = []
    resultDict = {'Areas' : areaResult, 'Circumferences' : circResult}
    for num in xrange(len(list)-1):
        areaResult.append(pi*(float(num)**2))
        circResult.append(2*pi*float(num))
    return resultDict
#     
resultMap = recordAreaAndCirc(radii)
# print resultMap
print "For circles with radii = %s\n\tAreas = %s\n\tCircumferences = %s\n\n" % (radii, resultMap['Areas'], resultMap['Circumferences'])
#   