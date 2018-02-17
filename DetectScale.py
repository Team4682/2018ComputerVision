import cv2
import numpy as np
from time import sleep
from networktables import NetworkTables as nt
import math

cap = cv2.VideoCapture(0)
ip = "10.46.82.2"
nt.initialize(server=ip)

#sd = nt.getTable("SmartDashboard")
s = nt.getTable('Scale')
sw = nt.getTable('Switch')
centerX = 320
centerY = 225
s.putNumber('View', 1)
def valueChanged(table, key, value, isNew):
     print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key,value, isNew))

def connectionListener(connected, info):
     print(info, '; connected=%s' % connected)

def computeCenter(M):
    m00 = int(M["m00"])
    m10 = int(M["m10"])
    m01 = int(M["m01"])
    
    if m00 == 0:
        print("Detected bad data from opencv")
        return (-1, -1)
    else:
        x = int(m10/m00)
        y = int(m01/m00)
        #print(x)
        #print(y)
        return(x,y)

while(True):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    canvas = frame
    
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130,255, 255])
    lower_red = np.array([160, 100, 100])
    upper_red = np.array([179, 255, 255])
    
    
    
    maskB = cv2.inRange(hsv, lower_blue, upper_blue)
    maskR = cv2.inRange(hsv, lower_red, upper_red)
    
    resB = cv2.bitwise_and(frame,frame, mask= maskB)
    resR = cv2.bitwise_and(frame,frame, mask= maskR)
    im2, contoursB, hierarchy1 = cv2.findContours(maskB, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    im3, contoursR, hierarchy2 = cv2.findContours(maskR, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #cnt = cv2.findContours(dst.copy())
    imge = frame
    
    blobB = max(contoursB, key=lambda el: cv2.contourArea(el), default=0)
    blobR = max(contoursR, key=lambda el: cv2.contourArea(el), default=0)
    MB = cv2.moments(blobB)
    MR = cv2.moments(blobR)
    
    if (len(contoursB) == 0) and (len(contoursR) == 0):
        print("Empty contours")
    else:
        pass
    
        
    
   

        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    centerB = computeCenter(MB)
    centerR = computeCenter(MR)
    
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 2, 100, minRadius=10, maxRadius=45)
    if circles is None:
        print("No Circles!")
        s.putNumber('View', 0)
        
    else:
        s.putNumber('View', 1)
        circles = np.round(circles[0, :]).astype("int")
        
        
        for(x,y, r) in circles:
            cv2.circle(canvas, (x, y), r, (255, 255, 0), 4)
            cv2.rectangle(canvas, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            
            
            
            
    cv2.circle(canvas, centerR, 2 ,(0,255,0), -1)
    cv2.circle(canvas, centerB, 2, (255, 0, 0), -1)
    
    xR, yR = centerR
    xB, yB = centerB
    
    cv2.imshow('Mask', maskR)
    cv2.imshow('Other', maskB)
    
    
    cv2.imshow('Can', canvas)
    k = cv2.waitKey(33)
    if k == ord('a'):
        break
cap.release()
cv2.destroyAllWindows()
