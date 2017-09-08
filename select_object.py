#Code by Timo Mueller @ EMM! Solutions GmbH - and other contributors, see: https://github.com/njoye/CNN-Tracker-v1

#In this file the object that should be tracked will be 
#selected, this can happen programmatically or by hand

# Import the required modules
import cv2
import argparse

def selectObject(coordinates={}):
	if(len(coordinates) == 4): #the user gave us coordinates for a tracking rectangle (x1, y1, x2, y2)
		pass #select the object and pass it back to the tracker
	else:
		pass#start something to select the object(s) by hand
