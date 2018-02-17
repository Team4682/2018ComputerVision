#This is the Python program to detect color during the FRC 2018 competition using the Adafruit TCS 34725 color sensor and the raspberry pi 3

#import necessary dependencies
from networktables import NetworkTables as nt
import time
import smbus
import Adafruit_TCS34725 as af
import os

ip = "10.46.82.2"
nt.initialize(server=ip)


#Create an instance of the Color Sensor
sensor = af.TCS34725()

sensor.set_interrupt(False)

while(1):
    
    r, g, b, c = sensor.get_raw_data()
    time.sleep(0.5)
    print("rgb=("+str(r)+", "+str(g)+", "+str(b)+")")
    #print(r)
    #print(g)
    #print(b)
    cls()
    colorTemp = af.calculate_color_temperature(r, g,b)
    lux = af.calculate_lux(r,g,b)
    print(str(colorTemp) + "k")
    print(str(lux) + " lux")
    




print(colorTemp)
print(lux)

sensor.set_interrupt(True)
sensor.disable()







