from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
led1 = LED(24)
led2 = LED(23)
led3 = LED(18)

win = Tk()
win.title("LED toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def led1Toggle():
    if led1.is_lit:
        led1.off()
        ledButton["text"] = "Turn LED  1 ON"
        
        
    else:
        led1.on()
        ledButton["text"] = "Turn LED 1 off"
        
def led2Toggle():
    if led2.is_lit:
        led2.off()
        ledButton["text"] = "Turn LED  2 ON"
        
        
    else:
        led2.on()
        ledButton["text"] = "Turn LED 2 off"

def led3Toggle():
    if led3.is_lit:
        led3.off()
        ledButton["text"] = "Turn LED  3 ON"
        
        
    else:
        led3.on()
        ledButton["text"] = "Turn LED 3 off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

led1Button = Button(win, text ="Turn led 1 ON" , font = myFont, command = led1Toggle, bg = 'red', height = 1, width = 24)
led1Button.grid(row = 0, column = 1)

led2Button = Button(win, text ="Turn led 2 ON" , font = myFont, command = led2Toggle, bg = 'green', height = 1, width = 24)
led2Button.grid(row = 1, column = 1)

led3Button = Button(win, text ="Turn led 3 ON" , font = myFont, command = led3Toggle, bg = 'white', height = 1, width = 24)
led3Button.grid(row = 2, column = 1)

exitButton = Button(win, text ="exit" , font = myFont, command = close , bg = 'bisque2', height = 1, width = 24)
exitButton.grid(row = 3, column = 1)

