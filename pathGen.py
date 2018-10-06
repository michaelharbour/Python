def pathGenFile():
  n = nuke.root()['name'].value()
  o = n.split("/")
  p = o[7].replace(".nk","")
  q = os.path.join( "/", o[1], o[2], o[3], o[4], o[5], "images", p, p+".####.tga")
  print q
  #nuke.thisNode()["message"].setValue("test")

pathGen()
