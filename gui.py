from tkinter import *
import sys
import time
from networktables import NetworkTables as nt
import logging



#ip Address
ip = "10.46.82.2"

'''Network Tables Communication'''

class NetworkTables:
    def __init__(self, sd, scale, switch):
        self.sd = nt.getTable("SmartDashboard")
        self.scale = nt.getTable("Scale")
        self.scale = nt.getTable("Switch")
        








'''GUI'''
Label(text='Control Panel', relief=RIDGE, width=15).grid(row=0, column=0)
Button(text="Post to SmartDashboard.", fg="Green", bg="White").grid(row=1, column=0)

labelStrings = ["x", "y", "z", "view", "color"]

nScaleEntries = 5
scaleEntries = []
for i in range(nScaleEntries):
    label = Label(text=labelStrings[i]).grid(row=i+2, column=0)

    entry = Entry().grid(row=i+2, column=1)
    scaleEntries.append(entry)

nSwitchEntries = 5
switchEntries = []
for i in range(nSwitchEntries):
    label = Label(text=labelStrings[i]).grid(row=i+2, column=2)
    entry = Entry().grid(row=i+2, column=3)
    switchEntries.append(entry)

nPostingEntries = 10
postingEntries = []
for i in range(nPostingEntries):
    entry = Entry().grid(row=i+2, column=4)
    postingEntries.append(entry)

Button(text="Stop", fg="Red", bg="White", command=quit).grid(row=13, column=0)


mainloop()
