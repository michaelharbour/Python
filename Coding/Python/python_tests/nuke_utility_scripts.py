# CLOSE OPEN CONTROL PANELS

s = nuke.allNodes()
for i in s :
  i.hideControlPanel()


# DISPLAY CHANNELS IN A SELECTED NODE

def showChannels():
  return '\n'.join(nuke.thisNode().channels())

node = nuke.selectedNode()
nuke.display('showChannels()', node, 'show channels for %s' % node.name())


# CREATE A CONTROL NODE WITH A CUSTOM KNOB
# AND LINK IT TO OTHER CREATED NODES

set cut_paste_input [stack 0]
version 11.3 v4
push $cut_paste_input
NoOp {
 name My_Python_Functions1
 tile_color 0xff0000ff
 note_font "Verdana Bold Bold Bold Bold Bold"
 note_font_size 12
 note_font_color 0xffffffff
 selected true
 xpos -590
 ypos 526
 addUserKnob {20 User}
 addUserKnob {22 closeControlPanels l "Close Open Panels" t "Hide open control panels" T "s = nuke.allNodes()\nfor i in s :\n  i.hideControlPanel()" +STARTLINE}
 addUserKnob {22 iso_mammal_hotkeys l "Available Mammal Hotkeys" t "This will reveal all of the Ctrl+Alt+Shift hotkeys not currently in use." T "# Bring in Nuke hotkeys\nimport string\nimport platform\n\nhostOS=platform.system()\nif \"Darwin\" in hostOS:\n    prefix = \"Cmd+Alt+Shift\"\nelse:\n    prefix = \"Ctrl+Alt+Shift\"\n\nmamHK = \[hotkey.strip() for hotkey in nuke.hotkeys().split(\"\\n\") if prefix in hotkey]\n\n# Cycle through A-Z comps and make a list of\n# ones that do not already exist.\n\nmyAZ = list(string.ascii_uppercase)\nmyUsedLetters = \[]\n\nfor x in myAZ:\n  mySearch = prefix + \"+\" + x\n  for item in mamHK:\n      if mySearch in item:\n        #print(mySearch + \" is already in use.\\n\")\n        myUsedLetters.append(x)\n\n# Print out a List of Mammal-style hotkeys not in use\n\nunused = list(set(myUsedLetters) ^ set(myAZ))\navail_hotkeys = \[]\nfor e in unused:\n  f = prefix + \"+\" + e\n  avail_hotkeys.append(f)\n\nnuke.message(\"The following Mammal Hotkeys \\nare available to you:\\n\\n\"+\"\\n\\t\".join(avail_hotkeys))\n\n#nuke.message(\"These letters are NOT in use: %r\" % (list(set(myUsedLetters) ^ set(myAZ))))" +STARTLINE}
 addUserKnob {22 displayChannels l "Display Selected Node's Channels" t "Open's a pannel and shows the channels that exist in the selected node(s)" T "def showChannels():\n  return '\\n'.join(nuke.thisNode().channels())\n\nnode = nuke.selectedNode()\nnuke.display('showChannels()', node, 'show channels for %s' % node.name())" +STARTLINE}
}


# REVERSE MOTIONBLUR KNOB VALUE IN SELECTED CLASS

# Get the Class of nodes that the user wants to change the motion blur values on

txt = nuke.getInput('Enter the type of nodes that you \nwant to reverse the\nmotion blur on.', '')

if txt or txt == 'all':
  x = nuke.allNodes(txt)
  unchanged = {} # Create a key:value empty dict to retain Tranform nodes w/ mb > 0 && < 1

  # Cycle through all Transform nodes
  for i in x:
    y = i.knob('motionblur').getValue()
    myName = i.knob('name').getValue()
    if y == 1:
      #print('one')
      i.knob('motionblur').setValue(0)
    elif y == 0:
      #print('zero')
      i.knob('motionblur').setValue(1)
    else:
      pull_value = str(y)
      unchanged.update({myName + " is unchanged.  MB = " : pull_value})

# Print the unchanged motion blur values and corresponding nodes to a pop up

myString = ''
for k, value in unchanged.iteritems():
  myString += "\n" + k + value + " \n"

nuke.message(myString)

# GENERATE CAMERA, SCANLINERENDER SETUP FROM PYTHON

# Create a camera scene exercize

#print(nuke.selectedNode().Class())

a = nuke.createNode('Sphere', inpanel=False)
b = nuke.createNode('Scene', inpanel=False)
clr = nuke.getColor()
b.knob('selected').setValue(False); b.knob('tile_color').setValue(clr)

user_scale = float(nuke.getInput('Enter the diameter of your sphere:'))

c = nuke.createNode('NoOp','name Control',inpanel=False)
c.knob('selected').setValue(False)
myArray = nuke.Array_Knob('myInt', 'Integer')
c.addKnob(myArray)
c.knob('myInt').setValue(user_scale)


a.knob('uniform_scale').setExpression('parent.Control.myInt')

d = nuke.createNode('ScanlineRender', inpanel=False)
d.knob('selected').setValue(False)

e = nuke.createNode('Camera', inpanel=False)

d.setInput(2, e)
d.setInput(1, b)

for n in nuke.allNodes():
  nuke.autoplaceSnap(n)

nuke.message("<font color='yellow'><b>All nodes have been successfully created</b>")


# MASS-INSERT NEW NODES ABOVE EXISITNG NODES USING NUKE.DEPENDENCIES()
'''Note: Write nodes need to be connected to script tree for dependencies() to work properly '''

ww=nuke.allNodes('Write') #We are looking for all Write nodes in our script
for a in ww:
  for y in a.dependencies():
    print(y.name())
    y.knob('selected').setValue(True)
    myCrop = nuke.createNode('Crop', inpanel=False)
    myCrop.knob('crop').setValue(False)
    sh=nuke.createNode('Shuffle', inpanel=False)
    sh.knob('selected').setValue(False)
for k in ww:
  nuke.autoplace(k) #Tidy up the node tree so the new nodes are in-line 

  '''another example of the same concept'''

  ww = nuke.allNodes('Write')
for a in ww:
  for b in a.dependencies():
    b.knob('selected').setValue(True)
    c = nuke.createNode('Crop', inpanel=False)
    c.knob('box').setExpression('format.w', 2);c.knob('box').setExpression('format.h', 3);
    d = nuke.createNode('Remove', inpanel=False)
    d.knob('channels').setValue('alpha')
    d.knob('selected').setValue(False)
for e in ww:
  nuke.autoplace(e)   


# USING LEN() IN YOUR SCRIPT TO IDENTIFY THE NUMBER OF NODES OF A CERTAIN TYPE

userInput = nuke.getInput('What type of nodes do you want to know the name of?').lower().capitalize()
myNum =  n=len(nuke.allNodes(myInput))

nuke.message("There are %i %s nodes in the script" % (myNum, userInput))

# GRABBING USER INPUT USING getInput() TO DRIVE SOME RESULT OVER THE SCRIPT

typeNode = nuke.getInput('What type of nodes do you want to change the font size for?').lower().capitalize()
fontSize = int(nuke.getInput('What size font would you like?'))

a = nuke.allNodes(typeNode)
for b in a:
  b.knob('note_font_size').setValue(fontSize)


# LESSON 3 PYTHON SCRIPTING FOR SMART AND CURIOUS COMPOSITORS 'HOMEWORK'

'''create a Python script that select all grade nodes in a script, 
creates a list and returns with the total number.'''

myList = []
myType = 'Grade'
for n in nuke.allNodes(myType):
  myList.append(n)

nuke.message("The total number of %s nodes in this script are %i." % (myType, len(myList)) )

'''Create a Python script that counts all selected nodes, 
then warns the user the last node will be deleted and then does it.'''

count = []
for x in nuke.selectedNodes():
    count.append(x)

myLen = len(count)
nuke.message("There are %i nodes selected.\nI am going to remove the last in the list" % myLen)

del count[-1]

newLen = len(count)

nuke.message("There are now %i nodes in the list" % newLen)


'''Create a Python script that delete all shuffle nodes in a script. This is something yous
hould be already familiar with since we did something similar with the basic functions we
already covered back to the first lesson, so please try with it and then provide a different
solution by using lists.'''

for n in nuke.allNodes('Shuffle'):
  nuke.delete(n)

# Or, using a list to cull these nodes 1st...

lis = []
for n in nuke.allNodes('Shuffle'):
  lis.append(n)

print(lis)

for i in lis:
  # if you want to just put the 'name' in the list you would use the nuke.toNode()
  # e.g. n = i.knob('name').value()
  #      o = nuke.toNode(n)
  #      nuke.delete(o)
  nuke.delete(i)


  '''  why not a further exercise ? Don't worry this is going to be very easy:
  just re-build the selection tool we have created but this time instead of creating 
  3 buttons intoa NoOp nodes  just create menus on top of your nuke interface.That's it !'''

  lis = []

def mySelect():
  for i in nuke.selectedNodes():
    lis.append(i)

  print(lis)

def myAppend():
  for i in nuke.selectedNodes():
    lis.append(i)

  print(lis)

def reSelect():
  for i in lis:
    i.knob('selected').setValue(True)
  

menubar = nuke.menu("Nuke")
m = menubar.addMenu("Michael Test")
m.addCommand("Select Nodes for List", "mySelect()")
m.addCommand("Add Nodes to List", "myAppend()")
m.addCommand("Selected Nodes in List", "reSelect()")


# QUICK AND DIRTY EXERCIZES USIGN MUKE.GETINPUT()

'''User selects nodes to extract from tree by name'''

rn=nuke.getInput("What type of nodes would you like to extract?", 'Be sure to capitalize your choice.')

for i in nuke.allNodes():
  i.knob('selected').setValue(False)

for i in nuke.allNodes(rn):
  i.knob('selected').setValue(True)
  nuke.extractSelected()
  nuke.autoplace(i)
  i.knob('selected').setValue(False)

'''A Simple Path Replacer that will move to affect all Read nodes'''

import os

inpa=nuke.getInput("path replacer", "type the path you want to replace")
inpb=nuke.getInput("path replacer", "type your new path")
readnds = nuke.allNodes("Read")
for x in readnds:
  pth = x.knob('file').value()
  npth = pth.replace(inpa,inpb)
  x.knob('file').setValue(npth)