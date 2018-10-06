#!/usr/bin/python
# -*- coding: utf-8 -*-
# Michael Harbour - Mammal Studios - Oct 16, 2014

import os
import sys
import getopt
import socket
import datetime
import getpass
import subprocess
import nuke

def rvioMakeQt():

	#Gather path variables from Nuke root.path
	
	f = int(nuke.root()['first_frame'].value())
	l = int(nuke.root()['last_frame'].value())
    #print str(f) + " - " + str(l)
	n = nuke.root()['name'].value()
	o = n.split("/")
	p = o[7].replace("_comp","")
	p = p.replace(".nk","")
	d = datetime.datetime.now().strftime("%m%d%y")
	g = ''.join([p, '_', d])
	
	#Assemble paths for rvio
	
	mkPathIn = os.path.join( "/", o[1], o[2], o[3], o[4], o[5], "images/comps", p, "2048x1152" )
	inPath = os.path.join( "/", mkPathIn, g + "." + str(f) + "-" + str(l) + "#.dpx")
	
	mkPathOut = os.path.join( "/", o[1], o[2], o[3], o[4], o[5], "images/comps", p, "1920x1080" )
	outPath = os.path.join( "/", mkPathOut, g+".mov")
	
	#Make Paths if they don't exist on (local ) file system
	
	if not os.path.exists(mkPathIn):
		os.makedirs(mkPathIn)
		print "making inPath: " 
		print inPath
	else:
		print "inPath already exists: "
		print inPath
		
	if not os.path.exists(mkPathOut):
		os.makedirs(mkPathOut)
		print "making outPath: " 
		print outPath
	else:
		print "outPath already exists: "
		print outPath

	#RVIO variables

	rvio = "/Applications/RV-4.2.0/RV64.app/Contents/MacOS/rvio"
	in_color = "-inlogc"
	out_color = "-outsrgb"
	codec = "-codec mjpeg"
	out_res = "-outres 1920 1080"
	rvio_inPath = inPath
	rvio_outPath = "-o "+outPath
	verbose = "-vv"

	#Assemble RVIO command and Execute

	print rvio , in_color , rvio_inPath , out_color ,  codec , out_res , rvio_outPath , verbose
	subprocess.call(['echo',  rvio , in_color , rvio_inPath , out_color ,  codec , out_res , rvio_outPath , verbose])



  
