import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import cv2


d1 = np.genfromtxt('thermalDataTest.csv', delimiter=',')
T1 = d1/100
Tref = 273.15 + 20

# Calibration Coefficients:
E = 44500
dt = 0.1

kg = 2.0  # Rate Constant (Needs to be calibrated)
q  = 6/7  # Kinetics Order (Needs to be calibrated)

te = 0

for i in range(50):
    dte = np.exp(-E/8.314*(1/T1 - 1/Tref))*dt
    te += dte
    P   = (kg * (1-q) * te)**(1/(1-q))

    cv2.imshow('PSI View', P)
    cv2.waitKey(1)
    ##cv2.waitKey(100)
    sleep(dt)





#plt.show()

print(P)
print(P.shape)




print('Analysis is DONE!')
