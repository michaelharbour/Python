# Bring in Nuke hotkeys

import string
import platform

hostOS=platform.system()
if "Darwin" in hostOS:
    prefix = "Cmd+Alt+Shift"
else:
    prefix = "Ctrl+Alt+Shift"

mamHK = [hotkey.strip() for hotkey in nuke.hotkeys().split("\n") if prefix in hotkey]

# Cycle through A-Z comps and make a list of
# ones that do not already exist.

myAZ = list(string.ascii_uppercase)
myUsedLetters = []

for x in myAZ:
  mySearch = prefix + "+" + x
  for item in mamHK:
      if mySearch in item:
        print(mySearch + " is already in use.\n")
        myUsedLetters.append(x)

# Print out a List of Mammal-style hotkeys not in use

nuke.message("These letters are NOT in use: %r" % (list(set(myUsedLetters) ^ set(myAZ))))


'''

BELOW IS MY HACKNIED WAY OF TRYING TO DO WHAT JANICE
TWEAKED INTO THE CODE ABOVE.  THIS IS JUST FOR REFERENCE.

# Bring in Nuke hotkeys

import string

a = nuke.hotkeys()
b = a.split("\n")


# Pull Mammal-specific hotkeys into a list

myList = []
for c in b:
  mamHK = "Ctrl+Alt+Shift+"
  if mamHK in c:
    myList.append(c.strip())


# Print out List of Mammal-used hotkeys

print("\n\nThis is myList\n")
for x in myList:
  print(x)

# Cycle through A-Z comps and make a list of
# ones that do not already exist.

myAZ = list(string.ascii_uppercase)
myEmptyList = []
myUsedLetters = []

for x in myAZ:
  mySearch = "Ctrl+Alt+Shift+" + x
  #print(mySearch)
  for item in mamHK:
      if mySearch in item:
        print(mySearch + " is already in use.\n")
        myUsedLetters.append(x)

# Print out a List of Mammal-style hotkeys not in use

print "These letters are NOT in use: %r" % (list(set(myUsedLetters) ^ set(myAZ)))

# Cycle through A-Z comps and make a list of
# ones that do not already exist.

#myAZ = list(string.ascii_uppercase)
#myEmptyList = []

#for x in myAZ:
  #mySearch = "Ctrl+Alt+Shift+" + x
  #print(mySearch)
  #if mySearch in myList:
   # print(mySearch + " is already in use.\n")
  #else:
    #myEmptyList.append(mySearch)

# Print out a List of Mammal-style hotkeys not in use

#print("\nThis is myEmptyList\n")

#for z in myEmptyList:
  #print(z)

'''