# import packages
import tkinter
from tkinter import *
import time
from djitellopy import Tello

# Drone Configuration
#d = Tello()
#d.connect()
#battery_level = d.get_battery()


# Methods & functions






def takeoff():
    pass


def land():
    pass

def right():
    pass

def left():
    pass




# Create and Config the Screen

w = tkinter.Tk()
w.geometry("600x400")






# create buttons & labels (titles)
titleLabel = Label(text="Drone Manette ", font=("Courier", 40, "bold"))
btnTackOff = Button(text = "", command="")
btnLand = Button(text="",command="")
btnRight = Button(text="",command="")
btnLeft = Button(text="",command="")
btnForward = Button(text="",command="")
btnBackward  =Button(text="",command="")



# Stick(pack) buttons on  the screen
titleLabel.pack()


w.mainloop()
