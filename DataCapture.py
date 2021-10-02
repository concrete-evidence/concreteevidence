import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt
from flirpy.camera.lepton import Lepton
import sys
import time
from time import sleep
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import csv

try:
    indexfile = open('data_index.txt','r')
    dindex = int(indexfile.read())
except:
    print('Could not initialize data index')


'''SPI Setup for ADC'''
# We can either use Software SPI or Hardware SPI. For software SPI we will
# use regular GPIO pins. Hardware SPI uses the SPI pins on the Raspberry PI
# Set the following variable to either HW or SW for Hardware SPI and Software
# SPI respectivly.
SPI_TYPE = 'HW'

# Software SPI Configuration
CLK     = 18    # Set the Serial Clock pin
MISO    = 23    # Set the Master Input/Slave Output pin
MOSI    = 24    # Set the Master Output/Slave Input pin
CS      = 25    # Set the Slave Select

# Hardware SPI Configuration
HW_SPI_PORT = 0 # Set the SPI Port. Raspi has two.
HW_SPI_DEV  = 0 # Set the SPI Device

# Instantiate the mcp class from Adafruit_MCP3008 module and set it to 'mcp'.
if (SPI_TYPE == 'HW'):
    # Use this for Hardware SPI
    mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(HW_SPI_PORT, HW_SPI_DEV))
elif (SPI_TYPE == 'SW'):
    # Use this for Software SPI
    mcp = Adafruit_MCP3008.MCP3008(clk = CLK, cs = CS, miso = MISO, mosi = MOSI)

'''Data Collection'''
NumInputs = 6 # Number of sensors attached to ADC

aread = pd.DataFrame(np.zeros([1,NumInputs+2]),columns = [i for i in range(NumInputs+2)])

try:
    while True:
        
        # Set up the Lepton thermal camera and take an image
        camera = Lepton()
        image = camera.grab() # Grab frame from camera 0
        print('Capture from FLIR Lepton thermal camera:')
        print(image)
       
        camera.close()

        pd.DataFrame(image).to_csv("Image_"+str(dindex)+'.csv')
        
        for i in range(2,NumInputs+2):
            data = mcp.read_adc(i) # read from ADC port i
            print('Analog data on port'+str(i)+':',str(data))
            aread[i] = data
        aread[0] = dindex
        aread[1] = time.time()
        
        aread.to_csv('thermistor_data.csv', mode='a', header=False, index=False)
        


        # Write new index to txt file
        indexfile = open('data_index.txt','w')
        dindex+=1
        indexfile.write(str(dindex))
        indexfile.close()
        
        sleep(1) # Wait 1 minute      
        
except KeyboardInterrupt:
    sys.exit()
    
            