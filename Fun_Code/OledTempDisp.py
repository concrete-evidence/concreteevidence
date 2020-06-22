import cv2
import numpy as np
import matplotlib.pyplot as plt
from flirpy.camera.lepton import Lepton

import time

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

def getRawData(port):
    camera = Lepton()
    rawData = camera.grab(port)
    return [rawData]

# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
def cleardisp():
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    disp.image(image)
    disp.show()
    time.sleep(0.1)
    return

padding = -2
top = padding
bottom = height - padding
x = 0

# Load default font.
font = ImageFont.load_default()
# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 9)

while True:

	rawData = getRawData(0)
    reshapedRawData = np.reshape(rawData,[120,160])
    tempsK = reshapedRawData / 100
    
    avgTempK = np.average(tempsK)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)


    # Write four lines of text.

    draw.text((x, top + 0), "Avg. Temp. In Frame:", font=font, fill=255)
    draw.text((x, top + 8), avgTempK + "K", font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.show()
    time.sleep(2)
