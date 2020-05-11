## Import Library
import numpy as np
import matplotlib.pyplot as plot
import cv2
from flirpy.camera.lepton import Lepton
from time import sleep

## INPUT Parameters
E  = 44500 # Activation Energy
kg = 2.0   # Rate Constant (Needs to be calibrated)
q  = 6/7   # Kinetics Order (Needs to be calibrated)

dt = 15.0  # Time interval between frames (seconds) 
t  = 0.0   # Initial physical time (hours)
te = t     # Intiial equivalent age (hours)

## Data Acquisition and Processing (degee K to PSI)
while(True):

	tempsK = getRawData(0) / 100 # Capture frame of temperatures in K
	dte = np.exp(-E/8.314*(1/T1 - 1/Tref))*(dt/3600)  ## Unit: hours
    	te += dte
	t  += dt
    	P   = (kg * (1-q) * te)**(1/(1-q)) ## Unit: PSI

    	cv2.imshow('PSI View', P)
    	cv2.waitKey(1)
    	sleep(dt)
	
	sleep(15) # Wait for a number of seconds between frames

    if cv2.waitKey(1) & 0xFF == ord('q'): # If 'q' key pressed
	savetxt('P.csv', data, delimiter=',')
	print('Terminate Time = ', t/3600, 'Hours')
		
        break # Exit while loop
		
## Get the data from an IR camera

def getRawData(port):
	camera = Lepton()
	rawData = camera.grab(port)
	return [rawData]
