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
