import tkinter as tk
from djitellopy import Tello

kn = Tello()
kn.connect()


window = tk.Tk()
window.geometry("650x400")
window.title("this is my mannette")

#battery = kn.get_battery()

def Up() :
    global battery
    print(battery)
    batteryL= tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_up(30)

def Down() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_down(30)

def Left() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_left(50)

def Right() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_right(50)

def Forward() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_forward(50)

def Back() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.move_back(50)

def takeoff():
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.takeoff()

def land() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.land()

def flipL() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.flip_left()

def flipR() :
    global battery
    print(battery)
    batteryL = tk.Label(text=battery)
    batteryL.grid(row=0, column=5, pady=10, padx=10)
    kn.flip_right()



imgUp = tk.PhotoImage(file="arrow-up.png").subsample(8, 8)
imgDown = tk.PhotoImage(file="arrow-down.png").subsample(8, 8)
imgLeft = tk.PhotoImage(file="arrow-left.png").subsample(8, 8)
imgRight = tk.PhotoImage(file="arrow-right.png").subsample(8, 8)
imgForward = tk.PhotoImage(file="img-Forward.png").subsample(8, 8)
imgBack = tk.PhotoImage(file="imgBack.png").subsample(8, 8)
imgTakeoff = tk.PhotoImage(file="imgTakeoff.png").subsample(8, 8)
imgLand = tk.PhotoImage(file="imgLand.png").subsample(8, 8)
imgfleft = tk.PhotoImage(file="flipl.png").subsample(8, 8)
imgfright = tk.PhotoImage(file="flipr.png").subsample(8, 8)

btnUp = tk.Button(image=imgUp, command=Up)
btnUp.grid(row=1, column=2, pady=10, padx=10)

btnDown = tk.Button(image=imgDown, command=Down)
btnDown.grid(row=3, column=2, pady=10, padx=10)

btnLeft = tk.Button(image=imgLeft, command=Left)
btnLeft.grid(row=2, column=1, pady=10, padx=10)

btnRight = tk.Button(image=imgRight, command=Right)
btnRight.grid(row=2, column=3, pady=10, padx=10)

btnForward = tk.Button(image=imgForward, command=Forward)
btnForward.grid(row=0, column=0, pady=10, padx=10)

btnBack = tk.Button(image=imgBack, command=Back)
btnBack.grid(row=1, column=0, pady=10, padx=10)

btntakeoff = tk.Button(image=imgTakeoff, command=takeoff)
btntakeoff.grid(row=0, column=4, pady=10, padx=10)

btnland = tk.Button(image=imgLand, command=land)
btnland.grid(row=1, column=4, pady=10, padx=10)

btnFleft = tk.Button(image=imgfleft, command=flipL)
btnFleft.grid(row=2, column=5, pady=10, padx=10)

btnFright = tk.Button(image=imgfright, command=flipR)
btnFright.grid(row=2, column=6, pady=10, padx=10)



window.mainloop()
