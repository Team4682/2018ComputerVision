#This is the Python program to detect color during the FRC 2018 competition using the Adafruit TCS 34725 color sensor and the raspberry pi 3

#import necessary dependencies
from networktables import NetworkTables as nt
import time
import smbus
import Adafruit_TCS34725 as af
import os

#Define the Global Variables:
#IP address and SD tables
#Initialize the Server as well.
'''-----------------------------------------------------------------------'''
ip = "10.46.82.2"
nt.initialize(server=ip)
sc = nt.getTable('Scale')
sw = nt.getTable('Switch')
'''------------------------------------------------------------------------'''
#Create an instance of the Color Sensor
sensor = af.TCS34725()

sensor.set_interrupt(False)

#Detect Color and Calculate Lumosity in infinite loop
'''------------------------------------------------------------------'''
while(1):
    
    r, g, b, c = sensor.get_raw_data()
    time.sleep(0.5)
    print("rgb=("+str(r)+", "+str(g)+", "+str(b)+")")
    
    colorTemp = af.calculate_color_temperature(r, g,b)
    lux = af.calculate_lux(r,g,b)
    print(str(colorTemp) + "k")
    print(str(lux) + " lux")
    if lux <= 9:
        sc.putNumber('View', 0)
        print("Lumosity is %s, Robot is not in the Scale Area" % (str(lux)))
    elif lux =< 10:
        sc.putNumber('View', 1)
        print("Lumosity is %s, Robot is in the Scale Area" % ((str(lux)))
'''---------------------------------------------------------------------'''
              
              
'''-----------------------------------------------------------------------'''
              #Enter sleep mode for Sensor
sensor.set_interrupt(True)
sensor.disable()







