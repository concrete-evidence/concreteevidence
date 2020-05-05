import numpy as np
import matplotlib.pyplot as plt
from flirpy.camera.lepton import Lepton

camera = Lepton()
image = camera.grab(0) # Grab frame from camera 0
print(image)

K=image/100 # Convert raw temp. array to temp. in Kelvin
print(K)
C=K-273.15 # Convert temp. in Kelvin to temp. in Celsius
print(C)
F=(1.8*C)+32 # Convert temp. in Celsius to temp. in Fahrenheit
print(F)

plt.imshow(image) # Display raw temperature data as an image

camera.close()
