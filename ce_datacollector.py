import numpy as np
import matplotlib.pyplot as plot
import cv2
from flirpy.camera.lepton import Lepton
from time import sleep

while(True):

	tempsK = getRawData(0) / 100 # Capture frame of temperatures in K
	

	# Do math here
	
	sleep(15) # Wait for a number of seconds between frames

    if cv2.waitKey(1) & 0xFF == ord('q'): # If 'q' key pressed
		
		# Print output here?
		
        break # Exit while loop
		

	  
	  
	  
def getRawData(port):
	camera = Lepton()
	rawData = camera.grab(port)
	return [rawData]