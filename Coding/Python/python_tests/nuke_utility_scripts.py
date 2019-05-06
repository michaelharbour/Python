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